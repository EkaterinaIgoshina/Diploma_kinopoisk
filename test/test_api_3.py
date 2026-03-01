import pytest
from kinopoisk_page_api_3 import CinemaPage
from dotenv import load_dotenv
import os
import allure


load_dotenv()
key = os.getenv("X-API-KEY")

@pytest.mark.api
@allure.feature("API тестирование - поиск фильмов")
@allure.story("Поиск фильмов за 2025 год")
@allure.title("Тест поиска фильма за 2025 год")
def test_search_movie_with_2025():
    base_url = "https://api.poiskkino.dev/"
    my_headers = {
        "Content-Type": "application/json; charset=utf-8",
        "X-API-KEY": key
    }

    cinema_page = CinemaPage(base_url, my_headers)
    with allure.step("Поиск фильмов за 2025 год"):
        movie_id = cinema_page.search_movie_by_2025()

    with allure.step("Проверка наличия фильмов"):
        if movie_id is None:
            print("Фильмы  за 2025 год не найдены.")
            assert False, "Фильмы за 2025 год не найдены."
        else:
            assert movie_id is not None, "Не удалось найти фильм за 2025 год."

