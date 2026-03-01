import requests
import allure
from typing import Optional, Dict, Union

class CinemaPage:
    def __init__(self, base_url: str, my_headers: Dict[str, Union[str, None]]) -> None:
        self.base_url: str = base_url
        self.my_headers: Dict[str, Union[str, None]] = my_headers

    @allure.story("Получение информации о фильме по ID")
    def get_movie_by_id(self, movie_id: str) -> Optional[str]:
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
                    else:
                        print(f"Ошибка API: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Произошла ошибка при запросе: {e}")
                return None
