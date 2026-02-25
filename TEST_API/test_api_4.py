import allure
from kinopoisk_page_api_4 import CinemaPage
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
@allure.title("API тестирование несуществующего ID")
@allure.severity("Critical")
def test_api_nonexistent_id() -> None:
    movie_id = "9999999"  # Не существующий ID
    expected_name = None  # Ожидаем, что результат будет None

    with allure.step("Запрос фильма по несуществующему ID"):
        actual_name = kino.get_movie_by_id(movie_id)

    assert actual_name == expected_name, f"Ожидалось название: '{expected_name}', фактическое: '{actual_name}'"