import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL_AFISHA = ''

DELAY = '1'


def get_content(url, params):
    headers = {'user-agent': UserAgent().chrome}
    resp = requests.get(url, params=params, headers=headers)
    return resp.text


def parse_afisha_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    movies = []
    for movie in soup.find_all('div', class_='new-list__item-info'):
        title = movie.find('a', class_='new-list__item-link').string
        year = movie.find('div', class_='new-list__item-status').string[:4]
        href = movie.find('a', class_='new-list__item-link')['href']
        movies.append({'title': title, 'year': year, 'href': href})
    return movies


def get_kinopoisk_rating(content, year):
    soup = BeautifulSoup(content, 'html.parser')
    try:
        for movie in soup.find_all('div', class_='element'):
            title_tag = movie.find('img', class_='flap_img')
            year_kp = title_tag.parent.parent.parent.find(
                'span',
                class_='year').string
            if year == year_kp:
                rating_kp = title_tag.parent.parent.parent.find(
                    'div',
                    class_='rating').string
                return float(rating_kp)
    except (TypeError, AttributeError):
        pass


def output_movies_to_console(movies, url_afisha):
    for i, movie in enumerate(movies[:10], start=1):
        print(
            '{0}. "{title}", {year}, rating: {rating}, schedule: '
            '{1}{href}'.format(i, 'https://www.afisha.ru/spb', **movie)
        )


if __name__ == '__main__':
    print('Afisha parsing...\n')
    url_afisha = 'https://www.afisha.ru/spb/schedule_cinema/?view=list'
    content_afisha = get_content(url_afisha, '')
    movies = parse_afisha_page(content_afisha)

    print('Kinopoisk parsing...\n')
    url_kinopoisk = 'https://www.kinopoisk.ru/index.php'
    for movie in movies:
        payload_kinopoisk = {'kp_query': '{} {}'.format(
            movie['title'],
            movie['year'])}
        content_kinopoisk = get_content(url_kinopoisk, payload_kinopoisk)
        movie['rating'] = get_kinopoisk_rating(content_kinopoisk, movie['year'])
    movies = sorted(
        movies,
        key=lambda x: x['rating'] if x['rating'] else 0,
        reverse=True)

    print('TOP-10 movies on view in Saint Petersburg:')
    output_movies_to_console(movies, url_afisha)
