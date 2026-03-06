from selenium.webdriver.common.by import By

class FAQLocators:
    ACTIVE_ANSWER_PANEL = (By.XPATH, ".//div[contains(@class,'accordion__panel') and not(@hidden)]")