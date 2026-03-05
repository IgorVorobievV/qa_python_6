import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from curl import *
from locators.base_locators import BaseLocators
from selenium.webdriver.common.by import By

class BasePage:

    @allure.step('Открываем браузер Mozilla Firefox')
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Открываем страницу {url} и соглашаемся с куки')
    def open(self, url):
        self.driver.get(url)
        self.find(BaseLocators.COOKIE_BUTTON).click()

    @allure.step('Находим локатор {locator}')
    def find(self, locator):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )
    
    @allure.step('Находим локатор с текстом {text}')
    def find_by_text(self, text):
        locator = (By.XPATH, ".//*[contains(text(),'" + text + "')]")
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step('Находим все локаторы {locator}')
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Кликаем локатор {locator}')
    def click(self, locator):
        self.find(locator).click()

    @allure.step('Кликаем локатор с текстом {text}')
    def click_by_text(self, text):
        self.find_by_text(text).click()

    @allure.step('Передаем в локатор {locator} текст {text}')
    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)    
   
    @allure.step('Получаем текст локатора {locator}')
    def get_text(self, locator):
        return self.find(locator).text
    
    @allure.step('Сравниваем url открытой страницы с {url}')
    def check_page(self, url):
        print(f'url: {url}')
        print(f'current_url: {self.driver.current_url}')
        self.wait.until(
            expected_conditions.url_to_be(url)
        )        
        return self.driver.current_url == url
    
    @allure.step('Получаем открытые окна')
    def get_open_window(self):
        current_windows = self.driver.window_handles
        print(f'open_windows:{current_windows}')
        return current_windows      

    @allure.step('Переключаемся в новое окно')
    def switch_new_window(self, current_windows):
        self.wait.until(
            expected_conditions.new_window_is_opened(current_windows)
        )
        new_windows = self.driver.window_handles
        new_window = [window for window in new_windows if window not in current_windows][0]
        self.driver.switch_to.window(new_window)