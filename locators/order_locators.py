from selenium.webdriver.common.by import By

class OrderLocators:
    NAME_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Имя')]")
    SURNAME_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Адрес')]")
    METRO_FIELD = (By.XPATH, ".//div[contains(@class,'select-search')]")
    METRO_FIRST_OPTION = (By.XPATH, ".//div[contains(text(),'Бульвар Рокоссовского')]")
    PHONE_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Телефон')]")
    NEXT_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_NextButton')]//button[contains(text(),'Далее')]")
    DATE_INPUT = (By.XPATH, ".//input[contains(@placeholder,'Когда привезти')]")
    DATE_SUBMIT = (By.XPATH, ".//div[contains(@class,'react-datepicker__day--selected')]")
    RENTAL_PERIOD_FIELD = (By.XPATH, ".//div[contains(@class,'Dropdown-root')]")
    RENTAL_PERIOD_OPTION = (By.XPATH, ".//div[contains(@class,'Dropdown-option')]")
    SUBMIT_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[contains(text(),'Заказать')]")
    CONFIRM_BUTTON = (By.XPATH, ".//div[contains(@class,'Order_Buttons')]//button[contains(text(),'Да')]")
    MODAL_HEADER = (By.XPATH, ".//div[contains(@class,'Order_ModalHeader')]")
    STATUS_BUTTON = (By.XPATH, ".//button[contains(text(),'Посмотреть статус')]")