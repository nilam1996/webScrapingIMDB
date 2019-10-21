from imdb_task_9 import*
from imdb_task_4 import*
import requests
from bs4 import BeautifulSoup
from pprint import pprint
def analyseMoviesLanguage(movies):
    generes=[]
    genreInDict={}
    for index in movies:
        genre=index["gener_list"]
        generes.extend(genre)
    for genre in generes:
        if genre not in genreInDict:
            genreInDict[genre]=1
        else:
            genreInDict[genre]=genreInDict[genre]+1
    return (genreInDict)
    
analyseLanguage=analyseMoviesLanguage(cachingData)
pprint()









