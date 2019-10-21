from pprint import pprint
from imdb_task_5 import all_data_detals 

def analyse_movies_language(movie_list):
    languages_movie = {}
    for index in movie_list:
        index["lang_list"]
        
        languages_list = index['lang_list']
        for language in languages_list:
            if(language not in languages_movie):
                languages_movie[language] = 1
            else:
                languages_movie[language] = languages_movie[language] + 1
    return (languages_movie)

analyse_lang=analyse_movies_language(all_data_detals)
pprint  (analyse_lang)
