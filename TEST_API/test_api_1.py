import allure
from kinopoisk_page_api_1 import CinemaPage
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("X-API-KEY")
base_url = "https://api.poiskkino.dev/"
my_headers = {
    "Content-Type": "application/json; charset=utf-8",
    "X-API-KEY": key
}

kino = CinemaPage(base_url, my_headers)

@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.title("API тестирование")
@allure.severity("Critical")
def test_api_1() -> None:
    movie_id = "7077099"
    expected_name = "Кракен"

    with allure.step("Запрос фильма по ID"):
        actual_name = kino.get_movie_by_id(movie_id)

    assert actual_name == expected_name, f"Ожидалось название: '{expected_name}', фактическое: '{actual_name}'"












