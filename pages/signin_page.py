from pages.base_page import BasePage
from data import URL
from locators.locators_signin_page import SigninLocators
import allure


class SigninPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу входа')
    def open_main_page(self):
        self.go_to_url(URL.MAIN_URL)

    @allure.step('Проверка загрузки страницы входа')
    def is_signin_page_loaded(self):
        return self.find_element(SigninLocators.SIGNIN_PAGE_TITLE)

    @allure.step('Нажатие на кнопку Создать аккаунт')
    def click_create_account_button(self):
        self.check_element_is_clickable(SigninLocators.LINK_SIGNUP)
        self.click_element(SigninLocators.LINK_SIGNUP)

    @allure.step('Отображение формы авторизации')
    def auth_form_is_displayed(self):
        return self.find_element(SigninLocators.FORM_AUTH)

    @allure.step('Заполнение формы авторизации')
    def auth_form_data_input(self,user_name, password):
        self.send_text(SigninLocators.EMAIL, user_name)
        self.send_text(SigninLocators.PASSWORD, password)

    @allure.step('Нажатие на кнопку Войти')
    def click_enter_account_button(self):
        self.check_element_is_clickable(SigninLocators.ENTER_BUTTON)
        self.click_element(SigninLocators.ENTER_BUTTON)


