from selenium.webdriver.common.by import By

class RootPageLocators:
    but_cookie = [By.ID, "rcc-confirm-button"]
    questions_block = [By.CLASS_NAME, "accordion__button"]
    ans_block = [By.CLASS_NAME, "accordion__panel"]