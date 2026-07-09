import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Переход по адресу')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента с ожиданием его видимости')
    def find_element(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Отображение элемента')
    def element_is_displayed(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def check_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        return self.find_element(locator)

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.find_element(locator).click()

    @allure.step('Ввод текста в элемент')
    def send_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        if element:
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
            except:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Найти неотображаемый элемент на странице')
    def find_invisible_element(self, locator):
        try:
            element = self.wait.until(expected_conditions.presence_of_element_located(locator))
            return element
        except:
            return None

    @allure.step('Прикрепление файла')
    def attach_file(self, locator, path):
        element = self.find_invisible_element(locator)
        if element:
            element.send_keys(str(path))
        else:
            raise AssertionError


