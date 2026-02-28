import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KinopoiskPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Зайти на главную страницу Кинопоиска')
    @allure.story('Открытие главной страницы')
    def open(self):
        self.driver.get('https://www.kinopoisk.ru')

    @allure.step("Поиск фильма 'Кракен'")
    @allure.story("Поиск фильма по названию")
    def search_movie(self, film_name):
        search_box = self.driver.find_element(By.CSS_SELECTOR, 'div.styles_searchFormContainer__qlnTa input')
        search_box.send_keys(film_name)
        search_box.submit()

    @allure.step("Ожидание загрузки страницы фильма")
    @allure.story("Ожидание загрузки страницы фильма по результатам поиска")
    def wait_for_movie_page(self):
        wait = WebDriverWait(self.driver, 30)
        first_result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.element .info .name a')))
        first_result.click()

    @allure.step("Проверка наличия элементов на странице фильма")
    @allure.story("Проверка элементов на странице фильма")
    def verify_movie_page_elements(self):
        wait = WebDriverWait(self.driver, 30)
        assert wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.film-poster'))), "Постер фильма не найден."

        # Проверка, что заголовок страницы содержит 'Кракен'
        assert "Кракен" in self.driver.title, (f"Ожидалось, что заголовок страницы будет содержать 'Кракен',"
                                               f" но найден: '{self.driver.title}'.")

