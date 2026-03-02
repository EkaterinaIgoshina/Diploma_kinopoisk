import allure
import os
import requests
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()
KINOPOISK_URL = os.getenv('KINOPOISK_URL')

class KinopoiskPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть главную страницу Кинопоиска")
    @allure.story("Открытие главной страницы")
    def open(self):
        response = requests.get(KINOPOISK_URL) #Проверяем статус ответа
        if response.status_code == 401:
            allure.attach("Authorization Error", "Доступ запрещен. Проверьте учетные данные.")
            raise Exception("Unauthorized access. Please check your credentials.")

        self.driver.get(KINOPOISK_URL)

    @allure.step("Перейти в раздел фильмов")
    @allure.story("Навигация в раздел фильмов")
    def go_to_movies_section(self):
        movies_section = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Фильмы']"))
        )
        movies_section.click()

    @allure.step("Нажать на 'Жанры'")
    @allure.story("Выбор жанров")
    def click_on_genres(self):
        genres_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Жанры"))
        )
        genres_button.click()


    @allure.step("Выбрать жанр 'Комедии'")
    @allure.story("Фильтрация по жанру 'Комедии'")
    def select_comedy_genre(self):
        comedy_genre = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Комедии"]'))
        )
        comedy_genre.click()

    @allure.step("Проверить наличие фильмов жанра 'Комедии'")
    @allure.story("Проверка фильмов по жанру")
    def check_movies_by_genre(self, genre="Комедии"):
        movie_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div[class*="movieCard"]')
        for movie in movie_elements:
            assert genre in movie.text, f"Фильм '{movie.text}' не относится к жанру '{genre}'."

