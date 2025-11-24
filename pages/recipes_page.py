from pages.base_page import BasePage
from locators.recipes_page_locators import RecipesPageLocators
from config.urls import URLs
from pathlib import Path
import random
import os
import allure


class RecipesPage(BasePage):
    TAG_LOCATORS = [
        RecipesPageLocators.TAG_BREAKFAST,
        RecipesPageLocators.TAG_LUNCH,
        RecipesPageLocators.TAG_DINNER,
    ]

    @allure.step("Открыть страницу создания рецепта")
    def open_create_recipe_page(self):
        self.open(URLs.CREATE_RECIPE)

    @allure.step("Ввести название рецепта: {name}")
    def enter_recipe_name(self, name):
        self.input_text(RecipesPageLocators.NAME_RECIPE, name)

    @allure.step("Выбрать тег")
    def select_random_tag(self):
        random_tag = random.choice(self.TAG_LOCATORS)
        self.click(random_tag)

    @allure.step("Добавить ингредиент: {ingredient_name}, колличество: {amount}")
    def add_ingredient(self, ingredient_name, amount):
        self.input_text(RecipesPageLocators.INGREDIENT_NAME, ingredient_name)
        suggestion_locator = RecipesPageLocators.choosing_an_ingredient(ingredient_name)
        self.wait.until(
            lambda d: len(d.find_elements(*suggestion_locator)) > 0,
            message=f"Не найдено предложения для ингредиента {ingredient_name}",
        )
        self.click(suggestion_locator)
        self.input_text(RecipesPageLocators.QUANTITY_INGREDIENT, amount)
        self.click(RecipesPageLocators.ADD_INGREDIENT)

    def add_ingredients(self, ingredients: list[dict]):
        for item in ingredients:
            self.add_ingredient(item["name"], item["amount"])

    @allure.step("Ввести время приготовления: {time}")
    def enter_cooking_time(self, time):
        self.input_text(RecipesPageLocators.COOKING_TIME, time)

    @allure.step("Ввести описание рецепта: {text}")
    def enter_description(self, text):
        self.input_text(RecipesPageLocators.RECIPE_DESCRIPTION, text)

    @allure.step("Загрузить изображение: {file_name}")
    def upload_image(self, file_name):
        file_path = Path(__file__).parent.parent / "assets" / file_name
        if not file_path.exists():
            raise FileNotFoundError(f"Файл {file_name} не найден по пути {file_path}")

        file_input = self.find_element(RecipesPageLocators.IMAGE_INPUT)
        file_input.send_keys(str(file_path.resolve()))

    @allure.step("Нажать кнопку 'Создать рецепт'")
    def click_create_recipe_button(self):
        self.click(RecipesPageLocators.CREATE_RECIPE_BTN)

    @allure.step("Создать рецепт: {name}")
    def create_recipe(
        self, name, ingredients, cooking_time, description, image_file="omlet.jpg"
    ):
        self.open_create_recipe_page()
        self.enter_recipe_name(name)
        self.select_random_tag()
        self.add_ingredients(ingredients)
        self.enter_cooking_time(cooking_time)
        self.enter_description(description)
        self.upload_image(image_file)
        self.click_create_recipe_button()

    @allure.step("Проверить, что рецепт с названием '{expected_title}' отображается")
    def wait_for_recipe_to_load(self, expected_title: str, timeout: int = 15) -> bool:
        try:
            self.wait.until(
                lambda d: self.find_visible_element(
                    RecipesPageLocators.RECIPE_TITLE
                ).text.strip()
                == expected_title,
                message=f"Не найден рецепт с названием '{expected_title}' за {timeout} секунд",
            )
            return True
        except Exception:
            return False
