from imdb_task_13 import*
from pprint import pprint

def analyse_co_actors(movies):
    cast_dict={}

    for cast in movies:
        cast_data=cast["cast"] 
        name=cast_data[0]["name"]
        id=cast_data[0]["imdb_id"]
        for movie in movies:
            cast_list=movie["cast"]
            if id==cast_list[0]["imdb_id"]:
                if id not in cast_dict:
                    cast_dict[id]={}
                    cast_dict[id]["frequent_co_actors"]=[]
                    cast_dict[id]["actor_name"]=name
                    cast_dict2={}
                    cast_dict2["num_movie"] = 1
                    cast_dict2["name"]=cast_data[1]["name"]
                    cast_dict2["imdb_id"]=cast_data[1]["imdb_id"]
                    cast_dict[id]["frequent_co_actors"].append(cast_dict2) 
                else:
                    number = 1
                    for cast in cast_dict[id]["frequent_co_actors"]:
                        if cast["imdb_id"] == cast_data[1]["imdb_id"]:
                            cast["num_movie"] = cast["num_movie"] + 1
                            
                        number = number + 1
                    if number == len(cast_dict[id]["frequent_co_actors"]):
                        cast_dict2={}
                        cast_dict2["name"] = cast_data[1]["name"]
                        cast_dict2["imdb_id"] = cast_data[1]["imdb_id"]
                        cast_dict[id]["frequent_co_actors"].append(cast_dict2)
    return cast_dict
cast_li=analyse_co_actors(cash_data)                      
pprint (cast_li) 