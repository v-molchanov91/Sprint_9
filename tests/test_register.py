import allure
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from config.urls import URLs


@allure.feature("Регистрация")
class TestRegister:
    @allure.title("Успешная регистрация нового пользователя")
    @allure.description(
        "1. Перейти на страницу регистрации.\n"
        "2. Заполнить все поля и нажать 'Создать аккаунт'.\n"
        "3. Проверить переход на страницу авторизации и отображение формы."
    )
    def test_user_can_register(self, driver, random_user):
        main_page = MainPage(driver)
        register_page = RegisterPage(driver)

        main_page.open_main_page()
        main_page.go_to_register()
        register_page.fill_register_form(random_user)
        register_page.click_create_account()
        register_page.wait_for_redirect_to_login()

        assert main_page.get_current_url() == URLs.MAIN
        assert main_page.is_login_form_visible()
