import allure
from pages.login_page import LoginPage
from config.urls import URLs


@allure.feature("Авторизация")
class TestLogin:
    @allure.title("Тест: успешная авторизация пользователя")
    @allure.description(
        "1. Выполнить вход.\n"
        "2. Проверить переход на главную и отображение кнопки 'Выход'."
    )
    def test_user_can_login(self, authenticated_user):
        driver = authenticated_user
        login_page = LoginPage(driver)

        current_url = login_page.get_current_url()
        assert (
            "recipes" in current_url
        ), f"Ожидался URL с /recipes, получен: {current_url}"
        assert login_page.is_logout_button_visible()
