import requests
import allure

class CinemaPage:
    def __init__(self, base_url, my_headers):  # Исправлено на __init
        self.base_url = base_url
        self.my_headers = my_headers

    def get_movie_by_id(self, movie_id):
        with allure.step(f"Запрос фильма по ID: {movie_id}"):
            try:
                response = requests.get(f'{self.base_url}v1.4/movie/{movie_id}', headers=self.my_headers)
                with allure.step(f"Проверка статус кода {response.status_code}"):
                    if response.status_code == 200:  # Успешный запрос
                        movie_data = response.json()
                        with allure.step(f"Проверка названия фильма: {movie_data['name']}"):
                            return movie_data['name']
                    elif response.status_code == 404:  # Фильм не найден
                        print("По этому ID ничего не найдено!")
                        return None
                    else:  # Обработка других ошибок
                        print(f"Ошибка API: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Произошла ошибка при запросе: {e}")
                return None