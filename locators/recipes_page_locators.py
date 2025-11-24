from selenium.webdriver.common.by import By


class RecipesPageLocators:
    RECIPE_SECTIONS = (By.XPATH, ".//a[text()='Рецепты']")
    CREATED_RECIPE = (By.XPATH, ".//a[text()='Создать рецепт']")
    NAME_RECIPE = (
        By.XPATH,
        ".//div[text()='Название рецепта']/following-sibling::input",
    )
    TAG_BREAKFAST = (By.XPATH, ".//span[text()='Завтрак']/preceding::button")
    TAG_LUNCH = (By.XPATH, ".//span[text()='Обед']/preceding::button")
    TAG_DINNER = (By.XPATH, ".//span[text()='Ужин']/preceding::button")
    INGREDIENT_NAME = (
        By.XPATH,
        ".//div[text()='Ингредиенты']/following-sibling::input",
    )
    QUANTITY_INGREDIENT = (
        By.XPATH,
        ".//div[contains(@class, 'AmountInputContainer')]/descendant::input",
    )
    ADD_INGREDIENT = (By.XPATH, ".//div[text()='Добавить ингредиент']")
    COOKING_TIME = (
        By.XPATH,
        ".//div[text()='Время приготовления']/following-sibling::input",
    )
    RECIPE_DESCRIPTION = (
        By.XPATH,
        ".//div[text()='Описание рецепта']/following-sibling::textarea",
    )
    IMAGE_INPUT = (By.XPATH, ".//input[@type='file']")
    CREATE_RECIPE_BTN = (By.XPATH, ".//button[text()='Создать рецепт']")
    RECIPE_TITLE = (By.XPATH, ".//h1")

    @staticmethod
    def find_recipe_in_recipe_section(recipe_name):
        return (By.XPATH, f".//a[text()='{recipe_name}']")

    @staticmethod
    def choosing_an_ingredient(ingredient):
        return (By.XPATH, f".//div[text()='{ingredient}']")
