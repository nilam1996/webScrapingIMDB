from imdb_task_1 import* 
from imdb_task_4 import*
from imdb_task_12 import*
from pprint import pprint
from os import path
import json
def scrapeAllMovieCast (movie_url):
    casts=[]
    for i in movie_url:
        link=i["link"]
        splitUrl=link.split("/")
        id=splitUrl[5]
        fileName="caching_cast_data/"+id
        if path.exists(fileName):
            with open (fileName,'r') as f:
                file_read = f.read()
                data = json.loads(file_read)
                casts.append(data)               
        else:
            print ("file not exists") 
            data=scrap_movie_details(link)
            movieCast=scrapeCasts(link)
            data["cast"]=movieCast
            with open(fileName,'w') as file1:
                jsonInStrings = json.dumps(data)
                file1.writ(jsonInStrings)
                casts.append(data)
            
    return casts
            
cashData=scrapeAllMovieCast(linkList)
# pprint(cash_data)
