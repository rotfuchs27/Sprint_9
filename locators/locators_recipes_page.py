from selenium.webdriver.common.by import By


class RecipesLocators:
    RECIPES_TITLE = By.XPATH, ".//h1[text()='Рецепты']"
    LINK_CREATE_RECIPES = By.XPATH, ".//a[text()='Создать рецепт']"
    CREATE_RECIPE_TITLE = By.XPATH, ".//h1[text()='Создание рецепта']"
    RECIPE_NAME = By.XPATH, ".//div[text()='Название рецепта']/following-sibling::input"
    INGREDIENT_NAME = By.XPATH, ".//div[text()='Ингредиенты']/following-sibling::input"
    INGREDIENT_AMOUNT = By.XPATH, ".//input[contains(@class, 'ingredientsAmountValue')]"
    INGREDIENTS_CONTAINER = By.XPATH, ".//div[contains(@class, 'ingredientsInputs')]/div[contains(@class, 'container')]"
    INGREDIENTS_NAMES = By.XPATH, "(.//div[contains(@class, 'ingredientsInputs')]/div[contains(@class, 'container')]/div)"
    ADD_INGREDIENT = By.XPATH, ".//div[text()='Добавить ингредиент']"
    COOKING_TIME = By.XPATH, ".//div[text()='Время приготовления']/following-sibling::input"
    RECIPE_DESCRIPTION = By.XPATH, ".//div[text()='Описание рецепта']/following-sibling::textarea"
    INPUT_FILE = By.XPATH, ".//input[@type='file']"
    CREATE_RECIPE_BUTTON = By.XPATH, ".//button[text()='Создать рецепт']"
    LINK_SIGNOUT = By.XPATH, ".//a[text()='Выход']"
    RECIPE = By.XPATH, ".//h1[text()='{data}']"
    RECIPE_CARD = By.XPATH, ".//div[contains(@class, 'single-card')]"

