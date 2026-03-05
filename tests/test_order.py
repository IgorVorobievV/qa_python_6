import pytest, allure

from pages.order_page import OrderPage
from data_gen import *

@allure.title('Проверить точку входа в сценарий - кнопка «Заказать» вверху страницы.')
@allure.description('На странице ищем кнопку «Заказать» вверху страницы и проверяем, что по клику происходит переход на страницу заказа.')
def test_success_order_entry_click_header_button(driver):
    page = OrderPage(driver)
    page.open_main_page()
    page.click_header_button()
    assert page.check_order_page()

@allure.title('Проверить точку входа в сценарий - кнопка «Заказать» внизу страницы')
@allure.description('На странице ищем кнопку «Заказать» внизу страницы и проверяем, что по клику происходит переход на страницу заказа.')
def test_success_order_entry_click_roadmap_button(driver):
    page = OrderPage(driver)
    page.open_main_page()
    page.click_roadmap_button()
    assert page.check_order_page()

@pytest.mark.parametrize('fields', order_fields)

@allure.title('Проверить заполнение формы заказа.')
@allure.description('На странице заказа заполняем все обязательные поля формы, поверяем появление окна подтверждения.')
def test_success_order(driver, fields):
    page = OrderPage(driver)
    page.open_order_page()
    page.filling_order_form(fields)
    assert  confirm_title in page.get_modal_header_text()

@allure.title('Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.')
@allure.description('На странице заказа заполняем все обязательные поля формы, подтверждаем заказ, поверяем появление окна с сообщением об успешном создании заказа.')
def test_success_show_success_modal_order(driver):
    page = OrderPage(driver)
    page.open_order_page()
    page.filling_order_form(order_fields[0])
    page.click_confirm_button()
    assert  success_title in page.get_modal_header_text()