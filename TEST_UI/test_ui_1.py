import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class TestMovieSearch:
    @pytest.fixture(scope="class")
    def setup(self):
        """Инициализация драйвера."""

        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        yield driver
        driver.quit()

    @allure.title("Проверка поиска фильма")
    @allure.description("Проверка функциональности поиска фильма на сайте Кинопоиск.")
    @allure.feature("Поиск фильма")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_movie(self, setup):
        """Тест для проверки поиска фильма."""
        driver = setup
        driver.get('https://www.kinopoisk.ru')

        wait = WebDriverWait(driver,20)

        with allure.step("Поиск фильма 'Кракен'"):
            # Найти строку поиска и ввести название фильма
            search_box = driver.find_element(By.CSS_SELECTOR, 'div.styles_searchFormContainer__qlnTa input')
            search_box.send_keys('Кракен')
            search_box.submit()

        with allure.step("Ожидание загрузки результатов поиска"):
           wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#block_left_pad > div')))


        with allure.step("Проверка наличия результатов"):
            results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.element')))
            assert len(results) > 0, "Результаты поиска не найдены."

        with allure.step("Проверка первого результата"):
            # Проверка, что первый результат соответствует ожиданиям
            first_result_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.element .info .name a'))).text
            assert 'Кракен' in first_result_name, f"Ожидалось, что '{first_result_name}' будет содержать 'Кракен'."





