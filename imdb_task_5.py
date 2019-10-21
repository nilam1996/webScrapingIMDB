from imdb_task_4 import scrap_movie_details
from imdb_task_1 import link_list1 as link
from pprint import pprint

def get_movie_list_details (movie_list):
    datas=[]
    for index in movie_list:
        movie_details= scrap_movie_details(index)

        datas.append(movie_details)
    return datas
all_data_detals=get_movie_list_details(link[0:10])
pprint(all_data_detals)
