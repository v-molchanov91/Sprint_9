from selenium.webdriver.common.by import By


class LoginPageLocators:
    PASSWORD = (By.XPATH, ".//input[@name='password']")
    USERNAME = (By.XPATH, ".//input[@name='email']")
    OPEN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    EXIT_BUTTON = (By.XPATH, ".//a[text()='Выход']")
