import requests
from bs4 import BeautifulSoup
from pprint import pprint
def scrape_top_list():
    top_movies_list=[]
    url="https://www.imdb.com/india/top-rated-indian-movies/"
    get_data=requests.get(url)
    soup=BeautifulSoup(get_data.text,"html.parser")
    div_data=soup.find("div",class_="lister")
    t_body=div_data.find("tbody",class_="lister-list")
    tr_data=t_body.find_all("tr")
    count=0
    for index in tr_data:
        dict_data={}
        position=count=count+1
        name= index.find("td",class_="titleColumn").a.get_text()
        year= index.find("td",class_="titleColumn").span.get_text()
        rating= index.find("td",class_="ratingColumn imdbRating").get_text()
        url= index.find("a")
        link="https://www.imdb.com/"+url["href"]
         
        dict_data["position"]=position
        dict_data["name"]=name
        dict_data["year"]=int(year[1:5])
        dict_data["rating"]=float(rating)
        dict_data["link"]=link
        top_movies_list.append(dict_data)
    return top_movies_list    
topMovies=scrape_top_list()
# pprint (top_movies)
# scrape_top_list()
def scrapeLink(movie_list):
    links=[]
    for index in movie_list:
        url= index['link']
        links.append(url)
    return links
linkList=scrapeLink(topMovies)
# pprint (link_list1)
    