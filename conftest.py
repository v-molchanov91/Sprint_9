import pytest
import os
import uuid
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.urls import URLs
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    selenoid_url = os.getenv("SELENOID_URL", "http://selenoid:4444/wd/hub")
    use_selenoid = os.getenv("USE_SELENOID", "true").lower() == "true"

    if use_selenoid:
        chrome_options = Options()
        chrome_options.set_capability("browserName", "chrome")
        chrome_options.set_capability("browserVersion", "128.0")
        chrome_options.set_capability(
            "selenoid:options",
            {
                "enableVNC": True,
                "enableVideo": False,
            },
        )
        driver = webdriver.Remote(command_executor=selenoid_url, options=chrome_options)
    else:
        chrome_options = Options()
        driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    driver.get(URLs.BASE)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def random_user():
    unique_id = str(uuid.uuid4())[:8]
    return {
        "email": f"{unique_id}@example.com",
        "username": f"user_{unique_id}",
        "password": "123password123",
        "first_name": f"User_{unique_id}",
        "last_name": f"Test_{unique_id}",
    }


@pytest.fixture(scope="function")
def authenticated_user(driver, random_user):
    main_page = MainPage(driver)
    register_page = RegisterPage(driver)
    login_page = LoginPage(driver)

    main_page.open_main_page()
    main_page.go_to_register()
    register_page.fill_register_form(random_user)
    register_page.click_create_account()
    register_page.wait_for_redirect_to_login()

    login_page.enter_username(random_user["username"])
    login_page.enter_password(random_user["password"])
    login_page.click_login_button()
    login_page.wait_for_login_success()

    return driver
