import requests
import allure


class CinemaPage:
    def __init__(self, base_url, my_headers):
        """Инициализация класса CinemaPage."""
        self.base_url = base_url
        self.my_headers = my_headers

    @allure.story("Поиск фильма по названию")
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
                        data = resp.json()
                        print(f"Ответ от API: {data}")
                        return data
                    elif resp.status_code == 404:
                        print("По этому названию ничего не найдено!")
                        return None
                    else:
                        print(f"Ошибка API: {resp.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Ошибка запроса: {e}")
                return None

    @allure.story("Поиск фильма за 2025 год")
    def search_movie_by_2025(self):
        """Тест поиска фильма  за 2025 год."""
        cinema_name = "Light of the World"

        with allure.step("Начинаем поиск фильма за 2025 год"):
            result = self.search_movie(cinema_name)
            if result:
                for movie in result.get("docs", []):
                    if movie.get("year") == 2025:
                        with allure.step(f"Найден фильм: "
                                         f"{movie.get('alternativeName')} за 2025 год."):
                            return movie.get("id")
            print("Фильмы  за 2025 год не найдены.")
            return None
