from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from curl import *

class HeaderPage(BasePage):
    
    def open_main_page(self):
        self.open(BASE_URL)

    def click_yandex_logo(self):
        self.click(HeaderLocators.YANDEX_LOGO)

    def click_scooter_logo(self):
        self.click(HeaderLocators.SCOOTER_LOGO)

    def check_main_page(self):
        return self.check_page(BASE_URL)
    
    def check_dzen_page(self):
        return self.check_page(DZEN_URL)