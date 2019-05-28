# TOP-10 movies on view

The script parses movies schedule in Saint Petersburg [from afisha.ru](https://www.afisha.ru/spb/schedule_cinema/?view=list), requests [Kinopoisk](https://www.kinopoisk.ru/) rating for each, sorts result and outputs TOP-10.


# How to Install

Python 3.6 and libraries from **requirements.txt** should be installed.

```bash

$ pip install -r requirements.txt
```


# Quickstart

1. Run **cinemas.py**.

```bash

$ python cinemas.py

Kinopoisk parsing, please wait:
. . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . .
TOP-10 movies on view in Saint Petersburg:
1. "Зеленая книга", 2018, rating: 8.3, shedule: https://www.afisha.ru/spb/movie/245280/
2. "Отель Мумбаи: Противостояние", 2018, rating: 8.1, shedule: https://www.afisha.ru/spb/movie/245926/
3. "Мстители: Финал", 2019, rating: 7.7, shedule: https://www.afisha.ru/spb/movie/223672/
4. "Аладдин", 2019, rating: 7.5, shedule: https://www.afisha.ru/spb/movie/232355/
5. "В метре друг от друга", 2019, rating: 7.3, shedule: https://www.afisha.ru/spb/movie/244784/
6. "Миа и белый лев", 2018, rating: 7.2, shedule: https://www.afisha.ru/spb/movie/244776/
7. "Братство", 2019, rating: 7.2, shedule: https://www.afisha.ru/spb/movie/243850/
8. "Джон Уик-3", 2019, rating: 7.0, shedule: https://www.afisha.ru/spb/movie/243683/
9. "Покемон. Детектив Пикачу", 2019, rating: 6.7, shedule: https://www.afisha.ru/spb/movie/243399/
10. "Красивый, плохой, злой", 2019, rating: 6.7, shedule: https://www.afisha.ru/spb/movie/244065/
. . . . . . . . . . . . . . . . . . . . . . . .

```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
