import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL_AFISHA = 'https://www.afisha.ru/spb'
URL_KINOPOISK = 'https://www.kinopoisk.ru/index.php'

def fetch_url(url, params):
    headers = {'user-agent': UserAgent().chrome}
    resp = requests.get(url, params=params, headers=headers)
    return resp.text


def parse_afisha_list():
    url = '{}/schedule_cinema/?view=list'.format(URL_AFISHA)
    soup = BeautifulSoup(fetch_url(url, ''), 'html.parser')
    movies = []
    for movie in soup.find_all('div', class_='new-list__item-info'):
        title = movie.find('a', class_='new-list__item-link').string
        year = movie.find('div', class_='new-list__item-status').string[0:4]
        href = movie.find('a', class_='new-list__item-link')['href']
        movies.append({'title': title, 'year': year, 'href': href})
    return movies


def fetch_movie_info(title, year):
    payload = {'kp_query': '{} {}'.format(title, year)}
    soup = BeautifulSoup(fetch_url(URL_KINOPOISK, payload), 'html.parser')

    try:
        for movie in soup.find_all('div', class_='element'):
            title_tag = movie.find('img', class_='flap_img')
            year_kp = title_tag.parent.parent.parent.find('span', class_='year').string
            if year == year_kp:
                rating_kp = title_tag.parent.parent.parent.find('div', class_='rating').string
                return float(rating_kp)

    except (TypeError, AttributeError):
        pass


def output_movies_to_console(movies):
    print('Kinopoisk parsing, please wait:')
    print('. '*len(movies))
    for movie in movies:
        rating_kp = fetch_movie_info(movie['title'], movie['year'])
        print('. ', end='', flush=True)
        movie['rating'] = rating_kp
        time.sleep(1)
    movies = sorted(movies, key=lambda x: x['rating'] if x['rating'] else 0, reverse=True)
    print('\nTOP-10 movies on view in Saint Petersburg:')
    for i, movie in enumerate(movies[:10], start=1):
        print('{0}. "{title}", {year}, rating: {rating}, schedule: {1}{href}'.format(i, URL_AFISHA, **movie))
    print('. '*len(movies))


if __name__ == '__main__':
    movies_list = parse_afisha_list()
    output_movies_to_console(movies_list)
