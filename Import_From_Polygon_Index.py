import json
import sys
import os


doc_id = 1


with open('from.json','r') as src:
	with open('to.json','w') as dst:

		data = json.load(src)
		all_hits = data['hits']
		all_docs = all_hits['hits']
		
		for doc in all_docs:
			single_doc = doc['_source']
			
			os.system("curl -XPOST 'http://localhost:1947/polygon/suggestion/" + str(doc_id) + "' -d '" + str(json.dumps(single_doc)) + "'")
			doc_id = doc_id + 1
			

			'''
			print str(single_doc)
			sys.exit()
			'''
			

			'''
			json.dump(single_doc, dst, indent=5)
			dst.write(",\n")
			doc_id = doc_id + 1
			'''