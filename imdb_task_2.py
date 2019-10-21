from imdb_task_1 import*
import requests
from bs4 import BeautifulSoup
from pprint import pprint 
def group_by_year(movies):
    years=[]
    dict_1={}
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    for i in years:
        dict_1[i]=[]

    for i in movies:
        years=i["year"]
        for j in dict_1:
            if j==years:
                dict_1[j].append(i)
    return dict_1        
            
year_wise=group_by_year(topMovies)
# pprint(year_wise)