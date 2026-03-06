import pytest, allure

from pages.faq_page import FAQPage
from data_gen import *

@pytest.mark.parametrize('ask,answer', faq)

@allure.title('Проверка когда нажимаешь на стрелочку, открывается соответствующий текст')
@allure.description('На странице ищем элемент с текстом-вопросом {ask} и проверяем, что по клику на него открывается блок с ответом {answer}')
def test_current_answer_in_faq(driver,ask,answer):
    page = FAQPage(driver)
    page.open_main_page()
    page.click_ask_button(ask)
    assert page.get_text_active_answer() == answer

