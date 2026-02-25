import requests
import allure

class CinemaPage:
    def __init__(self, base_url, my_headers):
        """Инициализация класса CinemaPage."""
        self.base_url = base_url
        self.my_headers = my_headers

    def search_movie(self, cinema_name):
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
                    else:
                        print(f"Ошибка API: {resp.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Ошибка запроса: {e}")
                return None

    def get_movie_id(self, cinema_name, ref_id):
        """Получение ID фильма по названию и референсному ID."""
        cinema_data = self.search_movie(cinema_name)
        if cinema_data:
            list_id = [movie.get('id') for movie in cinema_data.get("docs", [])]
            if ref_id in list_id:
                with allure.step(f"ID фильма = {ref_id}"):
                    return ref_id
        return None



