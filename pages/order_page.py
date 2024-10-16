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
    def go_to_site(self):
        return self.driver.get(ORDER_URL)

    def fill_name(self, name_str_in):
        self.fill_elem_text(OrderPageLocators.name, name_str_in)

    def fill_famil(self, famil_str_in):
        self.fill_elem_text(OrderPageLocators.famil, famil_str_in)

    def fill_addres(self, addres_str_in):
        self.fill_elem_text(OrderPageLocators.addres,addres_str_in)

    def fill_metro(self, metro_str_in):
        field_value = self.find_elem_with_wait(OrderPageLocators.metro)
        #field_value.send_keys(metro_str_in)  # заполняем нужным значением
        self.fill_elem_text(OrderPageLocators.metro, metro_str_in)

        actions = ActionChains(self.driver)  # и теперь чтобы оно заполнилось - имитируем стрелку вниз + энтер
        actions.move_to_element(field_value)
        actions.key_down(Keys.ARROW_DOWN)
        actions.key_up(Keys.ARROW_DOWN)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()

    def fill_mobile(self, mobile_str_in):
        self.fill_elem_text(OrderPageLocators.mobile,mobile_str_in)

    @allure.step('После того, как заполнили имя, фамилию и т.д. ждем кнопку далее')
    def go_but_next(self):
        self.click_elem_with_wait(OrderPageLocators.but_next)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.but_order))  # ждем следующей кнопки

    def fill_time(self, time_str_in):
        self.fill_elem_text(OrderPageLocators.time,time_str_in)

    def fill_duration(self, duration_str_in):
        self.click_elem_with_wait(OrderPageLocators.duration)
        self.driver.find_element(By.XPATH, "//div[text()='" + duration_str_in + "']").click()

    def fill_color(self):  # BLACK ONLY
        self.click_elem_with_wait(OrderPageLocators.color)

    @allure.step('После того, как заполнили данные по самокату (время, срок) - жмем "заказать"')
    def go_but_order(self):
        self.click_elem_with_wait(OrderPageLocators.but_order)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(OrderPageLocators.confirm_label))  # ждем следующей кнопки

    @allure.step('Подтверждаем заказ')
    def go_confirm(self):
        self.click_elem_with_wait(OrderPageLocators.but_confirm)

    def is_order_done(self):
        return self.find_elem_with_wait(OrderPageLocators.done_label).is_displayed