import allure
from pages.signin_page import SigninPage
from pages.recipes_page import RecipesPage
import pytest
from data import TEST_USER, TEST_PASSWORD

@allure.title('Проверка авторизации пользователя')
class TestSigninPage:

    @allure.title('Открыть страницу авторизации, авторизоваться, проверить загрузку страницы рецептов')
    @pytest.mark.parametrize('user_name, password', [(TEST_USER, TEST_PASSWORD)])
    def test_signin_page_auth_success(self, driver, user_name, password):
        signin_page = SigninPage(driver)
        recipes_page = RecipesPage(driver)

        signin_page.open_main_page()
        signin_page.is_signin_page_loaded()
        signin_page.auth_form_is_displayed()
        signin_page.auth_form_data_input(user_name, password)
        signin_page.click_enter_account_button()

        assert recipes_page.is_recipes_page_loaded()