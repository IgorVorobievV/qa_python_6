from selenium.webdriver.common.by import By

class BaseLocators:
    COOKIE_BUTTON = (By.XPATH, ".//button[contains(@class,'CookieButton')]")
    HEADER_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class,'Header_Header')]//button[contains(@class,'Button_Button')]")
    ROADMAP_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class,'Home_RoadMap')]//button[contains(@class,'Button_Button')]")