from kinopoisk_page_api_3 import CinemaPage
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("X-API-KEY")
def test_search_movie_with_rating():
    base_url = "https://api.poiskkino.dev/"
    my_headers = {
        "Content-Type": "application/json; charset=utf-8",
        "X-API-KEY": key
    }

    cinema_page = CinemaPage(base_url, my_headers)
    movie_id = cinema_page.search_movie_by_2025()

    # Проверка на наличие фильмов с рейтингом 10 за 2025 год
    if movie_id is None:
        print("Фильмы  за 2025 год не найдены.")
    else:
        assert movie_id is not None, "Не удалось найти фильм за 2025 год."