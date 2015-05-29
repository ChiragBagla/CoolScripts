#Python script to gather keywords for top grossing movies of the year 2014 from imdb. You can also check out for any year by just doing a small 
# editing in the source code.

import sys
import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.imdb.com/search/title?sort=boxoffice_gross_us,desc&year=2014,2014"


#Below fuction returns a set of tuples including names and links of movies on IMDB page

def get_top_grossing_movie_list(url):
    movies_list = []
    r = requests.get(url)
    for each_url in BeautifulSoup(r.text).select('.title a[href*="title"]'):
        movie_title = each_url.text 
        if movie_title != 'X':
            movies_list.append((movie_title, each_url['href']))
    return movies_list


#Below fuction returns a list of keywords associated with the movie.

def get_keywords_of_movie(url):
    keywords = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    tables = soup.find_all('table', class_='dataTable')
    table = tables[0]
    return [td.text for tr in table.find_all('tr') for td in tr.find_all('td')]


def main():

	movies = get_top_grossing_movie_list(URL);
	with open('run.csv', 'w') as run:
		csvwriter = csv.writer(run)
		for title, url in movies:
			keywords = get_keywords_of_movie('http://www.imdb.com{}keywords/'.format(url))
			csvwriter.writerow([title, keywords])

if __name__ == '__main__':
	sys.exit(main())
