import allure

from pages.header_page import HeaderPage

@allure.title('Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
@allure.description('На странице ищем логотип «Самоката» проверяем, что по клику происходит переход на главную страницу «Самоката».')
def test_success_click_scooter_logo_open_main_page(driver):
    page = HeaderPage(driver)
    page.open_main_page()
    page.click_scooter_logo()
    assert page.check_main_page()

@allure.title('Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
@allure.description('На странице ищем логотип Яндекса и проверяем, что по клику происходит переход на главную страницу Дзена.')
def test_success_click_yandex_logo_open_dzen_page(driver):
    page = HeaderPage(driver)
    page.open_main_page()
    current_windows = page.get_open_window()
    page.click_yandex_logo()
    page.switch_new_window(current_windows)
    assert page.check_dzen_page()