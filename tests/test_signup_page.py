import allure
from pages.signin_page import SigninPage
from pages.signup_page import SignupPage


@allure.title('Проверка страницы регистрации')
class TestSignupPage:

    @allure.title('Проверка перехода при клике на кнопку Создать аккаунт')
    def test_click_create_account_button_success(self, driver):
        main_page = SigninPage(driver)
        signup_page = SignupPage(driver)

        main_page.open_main_page()
        main_page.click_create_account_button()
        assert signup_page.is_signup_page_loaded()

    @allure.title('Проверка создания аккаунта')
    def test_click_create_account_success(self, driver):
        main_page = SigninPage(driver)
        signup_page = SignupPage(driver)
        signin_page = SigninPage(driver)

        main_page.open_main_page()
        main_page.click_create_account_button()
        signup_page.is_signup_page_loaded()
        signup_page.new_user_form_completion()

        assert signin_page.is_signin_page_loaded() and signin_page.auth_form_is_displayed()