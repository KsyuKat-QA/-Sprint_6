from sprint_6.pages.base_page import BasePage
from sprint_6.locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
import allure
from sprint_6.data import *
from sprint_6.locators.switch_locators import *
from selenium.webdriver.common.action_chains import ActionChains #для выбора станции метро
from selenium.webdriver.common.keys import Keys  #для выбора станции метро
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage(BasePage):
    @allure.step('Открыли браузер по ссылке ' +ORDER_URL )
    def go_to_site(self):
        return self.driver.get(ORDER_URL)

    @allure.step('Заполнили имя')
    def fill_name(self, name_str_in):
        self.fill_elem_text(OrderPageLocators.NAME, name_str_in)

    @allure.step('Заполнили фамилию')
    def fill_famil(self, famil_str_in):
        self.fill_elem_text(OrderPageLocators.FAMIL, famil_str_in)

    @allure.step('Заполнили адрес')
    def fill_addres(self, addres_str_in):
        self.fill_elem_text(OrderPageLocators.ADDRESS,addres_str_in)

    @allure.step('Заполнили станцию метро')
    def fill_metro(self, metro_str_in):
        field_value = self.find_elem_with_wait(OrderPageLocators.METRO)
        self.fill_elem_text(OrderPageLocators.METRO, metro_str_in)

        actions = ActionChains(self.driver)  # и теперь чтобы оно заполнилось - имитируем стрелку вниз + энтер
        actions.move_to_element(field_value)
        actions.key_down(Keys.ARROW_DOWN)
        actions.key_up(Keys.ARROW_DOWN)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()

    @allure.step('Заполнили номер телефона')
    def fill_mobile(self, mobile_str_in):
        self.fill_elem_text(OrderPageLocators.MOBILE,mobile_str_in)

    @allure.step('После того, как заполнили имя, фамилию и т.д. ждем кнопку далее')
    def go_but_next(self):
        self.click_elem_with_wait(OrderPageLocators.BUT_NEXT)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.BUT_ORDER))  # ждем следующей кнопки

    @allure.step('Заполнили дату для самоката')
    def fill_time(self, time_str_in):
        self.fill_elem_text(OrderPageLocators.TIME,time_str_in)

    @allure.step('Заполнили длительность')
    def fill_duration(self, duration_str_in):
        self.click_elem_with_wait(OrderPageLocators.DURATION)
        self.driver.find_element(By.XPATH, "//div[text()='" + duration_str_in + "']").click()

    @allure.step('Заполнили цвет (поле опциональное)')
    def fill_color(self):  # BLACK ONLY
        self.click_elem_with_wait(OrderPageLocators.COLOR)

    @allure.step('После того, как заполнили данные по самокату (время, срок) - жмем "заказать"')
    def go_but_order(self):
        self.click_elem_with_wait(OrderPageLocators.BUT_ORDER)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.CONFIRM_LABEL))  # ждем следующей кнопки

    @allure.step('Подтверждаем заказ')
    def go_confirm(self):
        self.click_elem_with_wait(OrderPageLocators.BUT_CONFIRM)

    @allure.step('Проверка завершения заказа')
    def is_order_done(self):
        return self.find_elem_with_wait(OrderPageLocators.DONE_LABEL).is_displayed