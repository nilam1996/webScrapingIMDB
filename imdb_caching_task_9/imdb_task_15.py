from imdb_task_12 import*
from imdb_task_1 import*
from pprint import pprint

def analysesActor(movies_list):
        cast_dict={}
        for movie in movies_list:
                link=movie["link"]
                cast_list=scrape_movie_cast(link)
                for actor_id in cast_list:
                        id=actor_id["imdb_id"]  
                        name=actor_id["name"]
                        for cast in cast_list:
                                if id == cast["imdb_id"]:
                                        if id not in castInDict:
                                                castInDict[id]={}
                                                castInDict[id]["name"] = name
                                                castInDict[id]["num_movie"] =1
                                        else:
                                                castInDict[id]["num_movie"] =castInDict[id]["num_movie"] +1
        return castInDict
                                                     
cast_list=analysesActor(top_movies)
pprint(cast_list)
        
        