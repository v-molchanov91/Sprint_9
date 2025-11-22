from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators
from config.urls import URLs
import allure


class RegisterPage(BasePage):
    @allure.step("Открыть страницу регистрации")
    def open_register_page(self):
        self.open(URLs.REGISTER)

    @allure.step("Ввести имя пользователя: {name}")
    def enter_first_name(self, name):
        self.input_text(RegisterPageLocators.FIRST_NAME, name)

    @allure.step("Ввести фамилию пользователя: {name}")
    def enter_last_name(self, name):
        self.input_text(RegisterPageLocators.LAST_NAME, name)

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username):
        self.input_text(RegisterPageLocators.USERNAME, username)

    @allure.step("Ввести почту пользователя: {email}")
    def enter_email(self, email):
        self.input_text(RegisterPageLocators.MAIL, email)

    @allure.step("Ввести пароль пользователя: {password}")
    def enter_password(self, password):
        self.input_text(RegisterPageLocators.PASSWORD, password)

    @allure.step("Нажать кнопку 'Создать аккаунт'")
    def click_create_account(self):
        self.click(RegisterPageLocators.CREATED_ACCOUNT)

    @allure.step("Ожидание перехода на страницу логина")
    def wait_for_redirect_to_login(self):
        self.wait_for_url_contains("/signin")

    @allure.step("Заполнить форму регистрации")
    def fill_register_form(self, user_data: dict):
        self.enter_first_name(user_data["first_name"])
        self.enter_last_name(user_data["last_name"])
        self.enter_username(user_data["username"])
        self.enter_email(user_data["email"])
        self.enter_password(user_data["password"])

    @allure.step("Зарегистрировать пользователя")
    def register_user(self, user_data: dict):
        self.open_register_page()
        self.fill_register_form(user_data)
        self.click_create_account()
