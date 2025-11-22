from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from config.urls import URLs
import allure


class LoginPage(BasePage):
    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open(URLs.MAIN)

    @allure.step("Ввести {username} в поле email")
    def enter_username(self, username):
        self.input_text(LoginPageLocators.USERNAME, username)

    @allure.step("Ввести {password} в поле password")
    def enter_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD, password)

    @allure.step("Нажать на кнопку войти")
    def click_login_button(self):
        self.click(LoginPageLocators.OPEN_BUTTON)

    @allure.step("Проверить, что кнопка Выход отображается")
    def is_logout_button_visible(self):
        return self.is_element_present(LoginPageLocators.EXIT_BUTTON)

    @allure.step("Ожидание успешной авторизации")
    def wait_for_login_success(self):
        self.find_visible_element(LoginPageLocators.EXIT_BUTTON)

    @allure.step("Проверить, что URL содержит /recipes")
    def is_on_recipes_page(self):
        return "/recipes" in self.get_current_url()

    @allure.step("Выполнить вход с {username}")
    def login(self, username, password):
        self.open(URLs.MAIN)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        self.wait_for_login_success()
