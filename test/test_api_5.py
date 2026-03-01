import pytest
import allure
from kinopoisk_page_api_5 import CinemaPage
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

@pytest.mark.api
@allure.feature("Сайт Кинопоиск - библиотека фильмов и сериалов")
@allure.story("Проверка API с использованием POST")
@allure.title("API тестирование с использованием POST")
@allure.severity("Critical")
def test_api_post() -> None:
    movie_id = "7077099"

    with allure.step("Запрос фильма по существующему ID через POST"):
        actual_name = kino.get_movie_by_id(movie_id)

    with allure.step("Выводим статус-код ответа"):
        print(f"Статус код ответа: {actual_name}")

    with allure.step("Проверка, что возвращается None, так как POST не должен возвращть фильм"):
        assert actual_name is None, (f"Ожидалось, что результат будет None,"
                                 f" но фактическое значение: '{actual_name}'")