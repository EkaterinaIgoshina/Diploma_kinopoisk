import pytest
import allure
from selenium import webdriver
from kinopoisk_page_ui_5 import KinopoiskPage


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Проверка работы с Телеканалами")
@pytest.mark.ui
class TestChannels:
    @allure.story("Навигация по разделу Телеканалы")
    @allure.title("Проверка перехода на страницу Телеканалы")
    def test_navigate_to_channels(self, setup):
        driver = setup
        kinopoisk_page = KinopoiskPage(driver)

        with allure.step("Открываем главную страницу Кинопоиска"):
            kinopoisk_page.open()

        with allure.step("Нажимаем на 'Телеканалы'"):
            kinopoisk_page.click_channels()

        with allure.step("Ожидаем загрузку страницы 'Смотреть каналы'"):
            kinopoisk_page.wait_for_channels_page()

        with allure.step("Проверить наличие заголовка 'Смотреть каналы'"):
            kinopoisk_page.check_channel_title()














