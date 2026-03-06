from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.order_locators import OrderLocators
from curl import *

class OrderPage(BasePage):
    
    
    def open_main_page(self):
        self.open(BASE_URL)

    def click_header_button(self):
        self.click(BaseLocators.HEADER_ORDER_BUTTON)

    def click_roadmap_button(self):
        self.click(BaseLocators.ROADMAP_ORDER_BUTTON)

    def check_order_page(self):
        return self.check_page(ORDER_URL)

    def open_order_page(self):
        self.open(ORDER_URL)

    def filling_order_form(self, order_fields):
        self.type(OrderLocators.NAME_INPUT, order_fields[0])
        self.type(OrderLocators.SURNAME_INPUT, order_fields[1])
        self.type(OrderLocators.ADDRESS_INPUT, order_fields[2])
        self.click(OrderLocators.METRO_FIELD)
        self.click(OrderLocators.METRO_FIRST_OPTION)
        self.type(OrderLocators.PHONE_INPUT, order_fields[3])
        self.click(OrderLocators.NEXT_BUTTON)
        self.type(OrderLocators.DATE_INPUT, order_fields[4])#05.03.2026
        self.click(OrderLocators.DATE_SUBMIT)
        self.click(OrderLocators.RENTAL_PERIOD_FIELD)
        self.click(OrderLocators.RENTAL_PERIOD_OPTION)
        self.click(OrderLocators.SUBMIT_BUTTON)
    
    def get_modal_header_text(self):
        return self.get_text(OrderLocators.MODAL_HEADER)
    
    def click_confirm_button(self):
        self.click(OrderLocators.CONFIRM_BUTTON)