import requests
import json
import string
import random

# POST polygons/_suggest
# {
#     "polygon" : {
#         "text":"la",
#         "completion" : {
#             "field" : "polygon_suggest",
#             "contexts": {
#                  "city":[
#                         { "context": "121" }
#                     ]
#             }
#         }
#     }
# }

# Clear the CACHE before the experiment
req = requests.post('http://localhost:7777/polygons/_cache/clear')

# Disable CACHING on our index also
req = requests.put('http://localhost:7777/polygons/_settings', { "index.cache.query.enable": "false" } )

const_city_boost = 3
const_all_boost = 1

for i in range(1,458):
	## Temporary Variables for POST Request ##
	request_payload = {}
	polygon = {}
	text = ""
	completion = {}
	field = "polygon_suggest"
	contexts = {}
	city = []

	#==== Have to be changed per request ===#
	city_id = i
	text = "a"
	# text = random.choice(string.letters)
	#=======================================#

	city.append( {"context":str(city_id), "boost":const_city_boost } )
	city.append( {"context":"All", "boost":const_all_boost } )

	contexts["city"] = city

	completion["field"] = field
	completion["contexts"] = contexts

	polygon["text"] = text
	polygon["completion"] = completion

	request_payload["polygon"] = polygon

	r = requests.post("http://localhost:7777/polygons/_suggest", data=json.dumps(request_payload))
	# print r.url
	# print request_payload
	# print "\n"
	# print r.text # Response Object
	# print r.status_code
	print city_id , "\t" , text , "\t" , r.elapsed.total_seconds() , "\t" , r.text , "\t" , r.status_code
	# print "\n" ,  r.text , "\n"


