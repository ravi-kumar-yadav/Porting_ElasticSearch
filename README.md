# Porting_ElasticSearch

###Download data from existing Hosted-Index into a local file###

#####Command#####

`curl -XPOST 'localhost:6667/polygon/_search' -d '    
{ "size":320000,    
  "query": {    
      "match_all": {}    
   }    
}' > search_result_src.txt`    

#####Format#####
`{    
   "took": 5,    
   "timed_out": false,    
   "_shards": {    
      "total": 5,    
      "successful": 5,    
      "failed": 0    
   },    
   "hits": {    
      "total": 318599,    
      "max_score": 1,    
      "hits": [    
         {    
            "_index": "polygon",    
            "_type": "suggestion",    
            "_id": "472",    
            "_score": 1,    
            "_source": {    
               "name": "Shukla Estate, Jogeshwari West, Mumbai, MMR, Maharashtra, India",    
               "city_id": 1,    
               "breadcrumb_score": 0.4,    
               "ftype_score": 6,    
               "score": {    
                  "buy": 15,    
                  "rent": 15,    
                  "pg": 15    
               },    
               "super_type": "polygon",    
               "city_uuid": "1ca99c33e3d8b987ccf1",    
               "type": "neighbourhood",    
               "id": 374681,    
               "uuid": "1609a75bf36cad0cb84c"    
            }    
         },    
         ......    
        ]    
    }    
}`    


###Read the above JSON file in python and load complete JSON in dictionary###

###Write Python code to convert the document structure (obtained from old search index) to the target search-index###

#####Format#####
`PUT polygons/polygon/3
{
    "polygon_suggest": [
        {
            "input" : ["Bharat Nagar, Noida, UP"],
            "contexts" : {
            "city": [ "Noida", "All" ],
            "services" : 
                    [   
                        {"buy": 2},
                        {"rent":5},
                        {"pg":7}
                    ]
            },
            "weight" : 35
        },
        ...
        ]
    }
}
`

###After forming document (in new format), it should make a "curl" call for each document to the new hosted-index service###


###See the result by firing search queries in new search-index###
	
            
