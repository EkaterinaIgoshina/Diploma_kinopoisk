from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class KinopoiskPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    @allure.step("Открыть главную страницу Кинопоиска")
    @allure.story("Навигация на главную страницу")
    def open(self):
        self.driver.get('https://www.kinopoisk.ru')

    @allure.step("Нажать на 'Телеканалы'")
    @allure.story("Переход к телеканалам")
    def click_channels(self):
        channels_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Телеканалы')))
        channels_link.click()

    @allure.step("Ожидание загрузки страницы 'Смотреть каналы'")
    @allure.story("Ожидание загрузкистраницы телеканалов")
    def wait_for_channels_page(self):
        self.wait.until(EC.title_contains("Смотреть каналы"))

    @allure.step("Проверить наличие заголовка 'Смотреть каналы'")
    @allure.story("Проверка заголовка страницы телеканалов")
    def check_channel_title(self):
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(), 'Смотреть каналы')]")))






