
import requests
from bs4 import BeautifulSoup
# https://movie.douban.com/top250
# https://movie.douban.com/top250?start=25


def getmovies():
    movies = []
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
               'Host': 'movie.douban.com'}

    for i in range(0, 10):
        link = 'http://movie.douban.com/top250?start=' + str(i * 25)
        result = requests.get(link, headers=headers, timeout=10)
        soup = BeautifulSoup(result.text , 'lxml')
        div_list = soup.find_all('div', class_='hd')
        for movie_name in div_list:
            movie = movie_name.a.span.text.strip()
            movies.append(movie)
    return movies
        

movies = getmovies()    
print(movies)





        
