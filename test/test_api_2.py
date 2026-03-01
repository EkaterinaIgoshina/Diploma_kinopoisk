import pytest
from kinopoisk_page_api_2 import CinemaPage
from dotenv import load_dotenv
import os
import allure


load_dotenv()
key = os.getenv("X-API-KEY")
@pytest.mark.api
class TestCinemaAPI:

    @pytest.fixture
    def cinema_api(self):
        base_url = "https://api.poiskkino.dev/"
        my_headers = {
            "Content-Type": "application/json; charset=utf-8",
            "X-API-KEY": key
        }
        return CinemaPage(base_url, my_headers)

    @allure.feature("API тестирование - получение ID фильма")
    @allure.story("Успешное получение ID фильма")
    @allure.title("Тест успешного получения ID фильма")
    @allure.severity("Critical")
    def test_get_movie_id_success(self, cinema_api):
        with allure.step("Получение ID фильма 'Царство небесное'"):
            cinema_id = cinema_api.get_movie_id("Царство небесное", ref_id=2602)

        with allure.step("Проверка ожидаемого ID"):
            assert cinema_id == 2602, "Ожидался ID = 2602"
    @allure.feature("API тестирование - получение ID фильма")
    @allure.story("Обработка случая, когда фильм не найден")
    @allure.title("Тест на случай, если фильм не найден")
    @allure.severity("Major")
    def test_get_movie_id_not_found(self, cinema_api):
        with allure.step("Получение ID несуществующего фильма 'Неизвестный фильм'"):
            cinema_id = cinema_api.get_movie_id("Неизвестный фильм", ref_id=999)

        with allure.step("Проверка, что ID равен None"):
            assert cinema_id is None, "Ожидался None для несуществующего фильма"

    @allure.feature("API тестирование - получение ID фильма")
    @allure.story("Обработка ошибок API")
    @allure.title("Тест для обработки ошибки API")
    @allure.severity("Critical")
    def test_get_movie_id_api_error(self, cinema_api):
        with allure.step("Получение ID фильма с неправильным ID"):
            cinema_id = cinema_api.get_movie_id("Царство небесное", ref_id=999)

        with allure.step("Проверка, что ID равен None"):
            assert cinema_id is None, "Ожидался None для фильма с неправильным ID"









