from selenium.webdriver.common.by import By

class RootPageLocators:
    BUT_COOKIE = [By.ID, "rcc-confirm-button"]
    QUESTIONS_BLOCK = [By.CLASS_NAME, "accordion__button"]
    ANS_BLOCK = [By.CLASS_NAME, "accordion__panel"]