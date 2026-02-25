import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class KinopoiskPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    @allure.step("Открыть главную страницу Кинопоиска")
    def open(self):
        self.driver.get('https://www.kinopoisk.ru')

    @allure.step("Нажать на 'Телеканалы'")
    def click_channels(self):
        channels_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Телеканалы')))
        channels_link.click()

    @allure.step("Ожидание загрузки страницы 'Смотреть каналы'")
    def wait_for_channels_page(self):
        self.wait.until(EC.title_contains("Смотреть каналы"))

    @allure.step("Проверить наличие заголовка 'Смотреть каналы'")
    def check_channel_title(self):
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(), 'Смотреть каналы')]")))  # Используем XPATH для проверки заголовка






