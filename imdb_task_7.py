from pprint import pprint
from imdb_task_5 import all_data_detals
def analyse_movies_directors (movie_list):
    director_dict={}
    director_list=[]
    for index in movie_list:
        director=index["director_li"]
        director_list.extend(director)
        
        for direct in director_list:
            if direct not in director_dict:
                
                director_dict[direct]=1
            else:
                director_dict[direct]=director_dict[direct]+1
    return director_dict
analysic_direct=analyse_movies_directors(all_data_detals)
pprint (analysic_direct)