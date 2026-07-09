import allure
import pytest
from pages.signin_page import SigninPage
from pages.recipes_page import RecipesPage
from helpers import DataGeneration
from data import TEST_USER, TEST_PASSWORD


@allure.title('Проверка страницы рецептов')
class TestRecipesPage:

    @allure.title('Проверка добавления рецепта авторизованым пользователем')
    @pytest.mark.parametrize('user_name, password', [(TEST_USER, TEST_PASSWORD)])
    def test_add_recipe_by_authorized_user_success(self, driver, user_name, password):
        signin_page = SigninPage(driver)
        recipes_page = RecipesPage(driver)

        signin_page.open_main_page()
        signin_page.is_signin_page_loaded()
        signin_page.auth_form_is_displayed()
        signin_page.auth_form_data_input(user_name, password)
        signin_page.click_enter_account_button()
        recipes_page.is_recipes_page_loaded()
        recipes_page.press_recipes_button()
        recipes_page.is_create_recipe_page_loaded()
        recipe_name = recipes_page.create_recipe()
        assert recipes_page.check_recipe_added(recipe_name)


