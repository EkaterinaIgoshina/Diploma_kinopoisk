import pytest
from selenium import webdriver
import allure
from kinopoisk_page_ui_3 import KinopoiskPage


@pytest.mark.ui
class TestMoviePage:
    @pytest.fixture(scope="class")
    def setup(self, request):
        """ Инициализация драйвера"""
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        request.cls.driver = driver
        yield driver
        driver.quit()


    @allure.title("Проверка наличия страницы фильма 'Кракен'")
    @allure.description("Проверка, что страница фильма 'Кракен' загружается корректно.")
    @allure.feature("Проверка страницы фильма")
    @allure.story("Проверка страницы фильма по названию")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_movie_page_exists(self, setup):
        """Тест для проверки наличия страницы фильма 'Кракен'."""
        driver = setup
        kinopoisk_page = KinopoiskPage(driver)
        kinopoisk_page.open()

        with allure.step("Поиск фильма 'Кракен'"):
            kinopoisk_page.search_movie('Кракен')

        with allure.step("Ожидание загрузки страницы фильма"):
            kinopoisk_page.wait_for_movie_page()

        with allure.step("Проверка наличия элементов на странице фильма"):
            kinopoisk_page.verify_movie_page_elements()

