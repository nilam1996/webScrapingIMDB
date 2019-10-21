from imdb_task_4 import*
from imdb_task_1 import*
from os import path
import json
from pprint import pprint
import random
import time 
def getDatausingTime(linkList):
    dataFromLink=[]
    for index in linkList:
        splitLink=index.split('/')
        linkId=splitLink[5]
        fileName='imdb_caching_task_9/'+linkId+'.json'
        if path.exists(fileName):
            with open (fileName,'r') as f:
                file_read = f.read()
                data = json.loads(file_read)
                dataFromLink.append(data)       
        else:
            print ("file not exists")
            data = scrap_movie_details(index)
            with open (fileName,"w") as file1:
                dataInJson=json.dumps(data)
                file1.write(dataInJson)
            randomNum=random.randint(1,3)
            timeSleep=time.sleep(randomNum)
            dataFromLink.append(data)
    return dataFromLink    
    
cachingData=getDatausingTime(linkList)
# pprint (caching_data)









