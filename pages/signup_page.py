from pages.base_page import BasePage
from data import URL
from locators.locators_signup_page import SignupLocators
import allure
from helpers import DataGeneration

class SignupPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на страницу создания аккаунта')
    def open_main_page(self):
        self.go_to_url(URL.MAIN_URL)

    @allure.step('Проверка загрузки страницы создания аккаунта')
    def is_signup_page_loaded(self):
        return self.find_element(SignupLocators.SIGNUP_PAGE_TITLE)

    @allure.step('Заполнение формы для нового пользователя')
    def new_user_form_completion(self):
        with allure.step('Ввод имени'):
            self.send_text(SignupLocators.FIRST_NAME, DataGeneration.generate_random_string(10))

        with allure.step('Ввод фамилии'):
           self.send_text(SignupLocators.LAST_NAME, DataGeneration.generate_random_string(10))

        with allure.step('Ввод имени пользоваетля'):
            self.send_text(SignupLocators.USERNAME, DataGeneration.generate_random_string(10))

        with allure.step('Ввод email'):
            self.send_text(SignupLocators.EMAIL, DataGeneration.generate_random_email())

        with allure.step('Ввод пароля'):
           self.send_text(SignupLocators.PASSWORD,DataGeneration.generate_random_string(10))

        with allure.step('Нажатие кнопки Создать аккаунт'):
            self.check_element_is_clickable(SignupLocators.CREATE_ACCOUNT_BUTTON)
            self.click_element(SignupLocators.CREATE_ACCOUNT_BUTTON)