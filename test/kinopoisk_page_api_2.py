import requests
import allure
from typing import Optional, Any, Dict

class CinemaPage:
    def __init__(self, base_url: str, my_headers: Dict[str, str]) -> None:
        """Инициализация класса CinemaPage."""
        self.base_url = base_url
        self.my_headers = my_headers

    @allure.story("Поиск фильма по названию")
    def search_movie(self, cinema_name: str) -> Optional[Dict[str, Any]]:
        """Запрос фильма по названию."""
        with allure.step(f"Запрос фильма по названию - {cinema_name}"):
            params = {
                "page": 1,
                "limit": 10,
                "query": cinema_name
            }
            try:
                resp = requests.get(f'{self.base_url}v1.4/movie/search', headers=self.my_headers, params=params)
                with allure.step(f"Проверка статус кода {resp.status_code}"):
                    if resp.status_code == 200:
                        return resp.json()
                    elif resp.status_code == 404:
                        print("По этому названию ничего не найдено!")
                        return None
                    elif resp.status_code == 401:
                        print("Ошибка авторизации: доступ запрещен.")
                        allure.attach("Authorization Error", "Доступ запрещен.Проверьте учетные данные.")
                        raise Exception("Unauthorized access. Please check your credentials.")
                    else:
                        print(f"Ошибка API: {resp.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Ошибка запроса: {e}")
                return None

    @allure.story("Получение ID фильма")
    def get_movie_id(self, cinema_name: str, ref_id: str) -> Optional[str]:
        """Получение ID фильма по названию и референсному ID."""
        with allure.step(f"Начинаем поиск ID для фильма '{cinema_name}'"
                         f" с референсным ID '{ref_id}'"
            ):
            cinema_data = self.search_movie(cinema_name)
            if cinema_data:
                list_id = [movie.get('id') for movie in cinema_data.get("docs", [])]
                if ref_id in list_id:
                    with allure.step(f"ID фильма = {ref_id}"):
                        return ref_id
        return None



