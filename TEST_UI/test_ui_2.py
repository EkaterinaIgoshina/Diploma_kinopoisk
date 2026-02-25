import allure
import pytest
from selenium import webdriver
from kinopoisk_page_ui_2 import KinopoiskPage

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Проверка работы фильтров в разделе фильмов")
class TestFilters:
    @allure.title("Проверка фильтров для жанра 'Комедии'")
    def test_genre_filter(self, setup):
        with setup as driver:
            kinopoisk_page = KinopoiskPage(driver)

            with allure.step("Открываем главную страницу"):
                kinopoisk_page.open()

            with allure.step("Переходим в раздел фильмов"):
                kinopoisk_page.go_to_movies_section()

            with allure.step("Нажимаем на 'Жанры'"):
                kinopoisk_page.click_on_genres()

            with allure.step("Выбираем жанр 'Комедии'"):
                kinopoisk_page.select_comedy_genre()

            with allure.step("Проверяем, что все фильмы имеют жанр 'Комедии'"):
                kinopoisk_page.check_movies_by_genre()




