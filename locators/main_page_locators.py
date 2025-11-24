from selenium.webdriver.common.by import By


class MainPageLocators:
    CREATED_ACCOUNT = (By.XPATH, ".//a[text()='Создать аккаунт']")
    OPEN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    RECIPES_BUTTON = (By.XPATH, ".//a[text()='Рецепты']")
    MAIN_PAGE = (By.XPATH, ".//h1[text()='Войти на сайт']")
