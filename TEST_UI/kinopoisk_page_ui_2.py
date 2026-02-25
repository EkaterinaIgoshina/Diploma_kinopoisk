import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KinopoiskPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть главную страницу Кинопоиска")
    def open(self):
        self.driver.get('https://www.kinopoisk.ru')

    @allure.step("Перейти в раздел фильмов")
    def go_to_movies_section(self):
        movies_section = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Фильмы']"))
        )
        movies_section.click()

    @allure.step("Нажать на 'Жанры'")
    def click_on_genres(self):
        genres_button = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Жанры"))
        )
        genres_button.click()


    @allure.step("Выбрать жанр 'Комедии'")
    def select_comedy_genre(self):
        comedy_genre = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Комедии"]'))
        )
        comedy_genre.click()

    @allure.step("Проверить наличие фильмов жанра 'Комедии'")
    def check_movies_by_genre(self, genre="Комедии"):
        movie_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div[class*="movieCard"]')
        for movie in movie_elements:
            assert genre in movie.text, f"Фильм '{movie.text}' не относится к жанру '{genre}'."

