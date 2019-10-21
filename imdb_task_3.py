from imdb_task_1 import*
from pprint import pprint
def group_by_decade(movies):
    dict1={}
    movies=[]
    for index in movies:
        lastDigit=index%10
        lastDigit = index-lastDigit
        if lastDigit not in movies:
            movies.append(lastDigit)
    movies.sort()
    for index in movies:
        dict1[index] = []
    for index in dict1:
        dec_year = index + 9
        for index1 in movies:
            if index1 <= dec_year and index1 >= index:
                for k in movies[index1]:
                    dict1[index].append(k)

    return (dict1)
decadeYear=group_by_decade(linkList)
pprint(decadeYear)

