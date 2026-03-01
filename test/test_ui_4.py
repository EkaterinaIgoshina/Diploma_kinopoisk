import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@pytest.mark.ui
class TestMovieSearch:
    @pytest.fixture(scope="class")
    def setup(self):
        """Инициализация драйвера."""

        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.maximize_window()
        yield driver
        driver.quit()


    @allure.title("Проверка поиска фильма по части названия")
    @allure.description("Проверка функциональности поиска фильма на сайте Кинопоиск по части названия.")
    @allure.feature("Поиск фильма")
    @allure.story("Поиск фильма по частичному названию")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_movie_partial_title(self, setup):
        """Тест для проверки поиска фильма по части названия."""
        driver = setup
        driver.get('https://www.kinopoisk.ru')

        wait = WebDriverWait(driver, 20)

        with allure.step("Поиск фильма 'Царство'"):
            search_box = driver.find_element(By.CSS_SELECTOR, 'div.styles_searchFormContainer__qlnTa input')
            search_box.send_keys('Царство')
            search_box.submit()

        with allure.step("Ожидание загрузки результатов поиска"):
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#block_left_pad > div')))

        with allure.step("Проверка наличия результатов"):
            results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.element')))
            assert len(results) > 0, "Результаты поиска не найдены."

        with allure.step("Проверка первого результата"):
            first_result_name = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.element .info .name a'))).text
            assert 'Царство' in first_result_name, f"Ожидалось, что '{first_result_name}' будет содержать 'Царство'."








