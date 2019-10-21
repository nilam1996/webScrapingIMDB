from imdb_task_1 import link_list1 as a
import requests
from bs4 import BeautifulSoup
from pprint import pprint 

def scrap_movie_details(movie_url):
        page = requests.get(movie_url)
        soup = BeautifulSoup(page.text,"html.parser")
        div_data=soup.find("div",class_="title_bar_wrapper").h1.get_text()
        movie_name1=div_data.split()
        movies_name=" ".join(movie_name1[:-1]) 
   
        sub_div = soup.find("div", class_ = "subtext")
       
        runtime = sub_div.find("time").get_text().strip()
        runtime_hours=int(runtime[0])*60
      
        if "min" in runtime:
                runtime_minutes = int(runtime[3:].strip("min"))
               
                movie_runtime = runtime_hours + runtime_minutes
            
        else:
                movie_runtime = runtime_hours
              


        gener = sub_div.findAll("a")
        gener.pop()
        gener_list=[]
        for i in gener:
            gen=i.get_text()
            gener_list.append(gen)
       
        bio=soup.find("div",class_="summary_text").get_text().strip()
        director=soup.find("div",class_="credit_summary_item")
        director_list = director.findAll("a")
        director_li=[]
        for i in director_list:
            director=i.get_text()
            director_li.append(director)
        contr_class=soup.find("div",class_="article",id="titleDetails")

        list_of_divs=contr_class.findAll("div",class_="txt-block")
        for div in list_of_divs:
                tag_h4 = div.findAll("h4")
                for text in tag_h4:
                    if "Language:" in text:
                            language_list=[]
                            tag_anchor = div.find_all("a")
                            for language in tag_anchor:
                                lang=language.get_text()
                                language_list.append(lang)
                    elif "Country:" in text:
                            tag_anchor = div.find_all("a")
                            for country1 in tag_anchor:
                                country=country1.get_text()
        post_image= soup.find("div",class_="poster").a["href"]
        poster_image_url = "https://www.imdb.com" + post_image
        movie_details_dict={}
        movie_details_dict["gener_list"]=gener_list
        movie_details_dict["lang_list"]=language_list
        movie_details_dict["poster_image_url"]=poster_image_url
        movie_details_dict["director_li"]= director_li
        movie_details_dict["movie_runtime"]= movie_runtime
        movie_details_dict["bio"]=bio
        movie_details_dict["country"]=country   
        movie_details_dict["name"]=movies_name
        return  movie_details_dict 
url1 =a[0]    
single_movie_details=scrap_movie_details(url1)
# pprint(single_movie_details)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  
