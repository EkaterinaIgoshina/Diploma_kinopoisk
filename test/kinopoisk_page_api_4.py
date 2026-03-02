import requests
import allure
from typing import Optional

class CinemaPage:
    def __init__(self, base_url: str, my_headers: dict) -> None:
        """Инициализация класса CinemaPage."""
        self.base_url = base_url
        self.my_headers = my_headers

    @allure.story("Получение информации о фильме по ID")
    def get_movie_by_id(self, movie_id: str) -> Optional[str]:
        """Запрос фильма по ID и получение названия."""
        with allure.step(f"Запрос фильма по ID: {movie_id}"):
            try:
                response = requests.get(f'{self.base_url}v1.4/movie/{movie_id}', headers=self.my_headers)
                with allure.step(f"Проверка статус кода {response.status_code}"):
                    if response.status_code == 200:
                        movie_data = response.json()
                        with allure.step(f"Проверка названия фильма: {movie_data['name']}"):
                            return movie_data['name']
                    elif response.status_code == 404:
                        print("По этому ID ничего не найдено!")
                        return None
                    elif response.status_code == 401:
                        print("Ошибка авторизации: доступ запрещен.")
                        allure.attach("Authorization Error", "Доступ запрещен. Проверьте учетные данные.")
                        raise Exception("Unauthorized access. Please check your credentials.")
                    else:
                        print(f"Ошибка API: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Произошла ошибка при запросе: {e}")
                return None
