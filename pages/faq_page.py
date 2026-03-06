from pages.base_page import BasePage
from locators.faq_locators import FAQLocators
from curl import *

class FAQPage(BasePage):
    
    
    def open_main_page(self):
        self.open(BASE_URL)

    def click_ask_button(self, text):
        self.click_by_text(text)

    def get_text_active_answer(self):
        return self.get_text(FAQLocators.ACTIVE_ANSWER_PANEL)