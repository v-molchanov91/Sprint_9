from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FIRST_NAME = (By.XPATH, ".//input[@name='first_name']")
    LAST_NAME = (By.XPATH, ".//input[@name='last_name']")
    USERNAME = (By.XPATH, ".//input[@name='username']")
    PASSWORD = (By.XPATH, ".//input[@name='password']")
    MAIL = (By.XPATH, ".//input[@name='email']")
    CREATED_ACCOUNT = (By.XPATH, ".//button[text()='Создать аккаунт']")
