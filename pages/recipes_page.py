from pages.base_page import BasePage
from locators.locators_recipes_page import RecipesLocators
import allure
from helpers import DataGeneration
from pathlib import Path


class RecipesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверка загрузки страницы рецептов')
    def is_recipes_page_loaded(self):
        return self.find_element(RecipesLocators.RECIPES_TITLE)

    @allure.step('Нажатие на кнопку Созадть рецепт')
    def press_recipes_button(self):
        self.check_element_is_clickable(RecipesLocators.LINK_CREATE_RECIPES)
        self.click_element(RecipesLocators.LINK_CREATE_RECIPES)

    @allure.step('Проверка загрузки страницы создания рецепта')
    def is_create_recipe_page_loaded(self):
        return self.find_element(RecipesLocators.CREATE_RECIPE_TITLE)

    @allure.step('Создание рецепта')
    def create_recipe(self):

        with allure.step('Ввод названия рецепта'):
            recipe_name = DataGeneration.generate_random_string(30)
            self.send_text(RecipesLocators.RECIPE_NAME, recipe_name)

        with allure.step('Выбор ингредиента'):
            self.send_text(RecipesLocators.INGREDIENT_NAME, 'шоколад')
            self.element_is_displayed(RecipesLocators.INGREDIENTS_CONTAINER)
            ingredient = self.find_element(RecipesLocators.INGREDIENTS_NAMES)
            ingredient.click()

        with allure.step('Ввод количества ингредиента'):
            self.send_text(RecipesLocators.INGREDIENT_AMOUNT, 200)

        with allure.step('Добавление ингредиента'):
            self.click_element(RecipesLocators.ADD_INGREDIENT)

        with allure.step('Ввод времени приготовления'):
            self.send_text(RecipesLocators.COOKING_TIME, 45)

        with allure.step('Ввод описания рецепта'):
            self.send_text(RecipesLocators.RECIPE_DESCRIPTION,DataGeneration.generate_random_string(150))

        with allure.step('Загрузка фото рецепта'):
            base_dir = Path(__file__).parent.parent
            file_path = (base_dir / "assets" / "recipe_image.jpg").resolve()
            self.attach_file(RecipesLocators.INPUT_FILE, str(file_path))

        with allure.step('Нажатие кнопки Создать рецепт'):
            self.scroll_to_element(RecipesLocators.CREATE_RECIPE_BUTTON)
            self.check_element_is_clickable(RecipesLocators.CREATE_RECIPE_BUTTON)
            self.click_element(RecipesLocators.CREATE_RECIPE_BUTTON)

        return recipe_name

    @allure.step('Проверка создания рецепта')
    def check_recipe_added(self, recipe_name):
        by_type, locator = RecipesLocators.RECIPE
        recipe_title_locator = by_type, locator.format(data=recipe_name)
        conditions = [
            self.element_is_displayed(RecipesLocators.RECIPE_CARD),
            self.element_is_displayed(recipe_title_locator)
        ]
        return all(conditions)

