from imdb_task_9 import*
from pprint import pprint
from imdb_task_1 import*
def analyselanguageAndDirector(movie_list):
    directorInDict={}
    for link in movie_list:
        directors = link["director_li"]
        for director in  directors:
            if director not in directorInDict:
                directorInDict[director]={}
                for index in movie_list:
                    directors=index["director_li"]
                    langList=index["lang_list"]
                    for lang in langList:
                        if  director in directors:
                            if lang not in directorInDict[director]:
                                directorInDict[director][lang] = 1
                            else:
                                directorInDict[director][lang] = directorInDict[director][lang] + 1
    return (directorInDict)
moviesLanguageAndDirector = analyselanguageAndDirector(cachingData)
pprint(moviesLanguageAndDirector)