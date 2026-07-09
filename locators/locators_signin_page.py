from selenium.webdriver.common.by import By


class SigninLocators:
    SIGNIN_PAGE_TITLE = By.XPATH, ".//h1[text()='Войти на сайт']"
    LINK_RECIPES = By.XPATH, ".//a[text()='Рецепты']"
    LINK_SIGNIN = By.XPATH, ".//a[text()='Войти']"
    LINK_SIGNUP = By.XPATH, ".//a[text()='Создать аккаунт']"
    EMAIL = By.XPATH, ".//input[@name='email']"
    PASSWORD = By.XPATH, ".//input[@name='password']"
    ENTER_BUTTON = By.XPATH, ".//button[text()='Войти']"
    FORM_AUTH = By.XPATH, ".//form[.//input[@name='email'] and .//input[@name='password'] and .//button[text()='Войти']]"

