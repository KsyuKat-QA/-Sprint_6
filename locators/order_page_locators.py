from selenium.webdriver.common.by import By

class OrderPageLocators:
    name = [By.XPATH, "//input[@placeholder='* Имя']"]
    famil = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    addres = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    mobile = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    but_next = [By.XPATH, "//button[text()='Далее']"]

    time = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    duration = [By.CLASS_NAME, "Dropdown-arrow"]
    color = [By.XPATH, "//input[@id='black']"]
    but_order = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    confirm_label = [By.XPATH, "//div[text()='Хотите оформить заказ?']"]
    but_confirm = [By.XPATH, "//button[text()='Да']"]

    done_label = [By.XPATH, "//div[text()='Заказ оформлен']"]