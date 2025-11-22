from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from config.urls import URLs
import allure


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(URLs.BASE)

    @allure.step("Перейти на страницу логина")
    def go_to_login(self):
        self.click(MainPageLocators.OPEN_BUTTON)

    @allure.step("Перейти на страницу регистрации")
    def go_to_register(self):
        self.click(MainPageLocators.CREATED_ACCOUNT)

    @allure.step("Проверить, что форма логина отображается")
    def is_login_form_visible(self):
        return self.is_element_present(MainPageLocators.MAIN_PAGE)
