import requests
from bs4 import BeautifulSoup
from imdb_task_1 import*
import json
from os import path

def  scrapeCasts (movies):
    casts=[]
    splitId=movies.split("/")
    Id=splitId[5]
    fileName="cast_cash_250/"+Id+"_cast.json"
    if path.exists(fileName):
        with open(fileName,"r") as f1:
            file_read=f1.read()
            data=json.loads(file_read)
        return data
    else:
        print ("file not exists")
        get_data=requests.get(movies)
        soup=BeautifulSoup(get_data.text,"html.parser")
        cast_t_body=soup.find("table",class_="cast_list")
        find_td=cast_t_body.findAll('td',class_='')
        for index in find_td:
            dataInDict={}
            links=index.a["href"]
            splitLink=links.split("/")
            id=splitLink[2]
            acter=index.a.get_text()
            dataInDict["imdb_id"]=id
            dataInDict["name"]=acter
            casts.append(dataInDict)
            
            with open(fileName,"w") as file1:
                json_data=json.dumps(casts)
                file1.write(json_data)

    return casts
url=linkList[0]["link"]
cast = scrapeCasts(url)  
# pprint(cast)

                
                
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
