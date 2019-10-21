from pprint import pprint
import os.path
import json
from imdb_task_1 import*
from imdb_task_4 import scrap_movie_details
def caching_imdb_data(movie_url):
    for index in movie_url[:2]:
        splitLinks=index.split('/')
        Id=splitLinks[5]
        fileName='caching_all_data/'+Id+'.json'
        if os.path.exists(fileName):
            with open (fileName,'r') as f:
                file_read = f.read()
                data1=json.loads(file_read)
            return data1
        else:
            print ("file is not exists")
            data=scrap_movie_details(index)
            with open(fileName, 'w') as file1:
                json_strings = json.dumps(data)
                file1.write(json_strings)      
caching_data=caching_imdb_data(linkList)
# pprint (caching_data)










