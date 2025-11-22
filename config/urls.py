from urllib.parse import urljoin


BASE_URL = "https://foodgram-frontend-1.prakticum-team.ru/"


class URLs:
    BASE = BASE_URL
    MAIN = urljoin(BASE_URL, "/signin")
    REGISTER = urljoin(BASE_URL, "/signup")
    RECIPE = urljoin(BASE_URL, "/recipes")
    CREATE_RECIPE = urljoin(BASE_URL, "/recipes/create")

    @staticmethod
    def recipe_detail(recipe_id: int) -> str:
        return urljoin(BASE_URL, f"/recipes/{recipe_id}/")
