from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    FAMIL = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    MOBILE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUT_NEXT = [By.XPATH, "//button[text()='Далее']"]

    TIME = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    DURATION = [By.CLASS_NAME, "Dropdown-arrow"]
    COLOR = [By.XPATH, "//input[@id='black']"]
    BUT_ORDER = [By.XPATH, "//button[contains(@class,'Button_Button__ra12g ') and text()='Заказать']"]

    CONFIRM_LABEL = [By.XPATH, "//div[text()='Хотите оформить заказ?']"]
    BUT_CONFIRM = [By.XPATH, "//button[text()='Да']"]

    DONE_LABEL = [By.XPATH, "//div[text()='Заказ оформлен']"]