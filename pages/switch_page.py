from sprint_6.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from sprint_6.data import *
from sprint_6.locators.switch_locators import SwitchPageLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure

class SwitchPage(BasePage):
    @allure.step('Открыли браузер по ссылке ' + ORDER_URL)
    def go_to_site(self):
        return self.driver.get(ORDER_URL)

    @allure.step('Кликаем по логу самоката')
    def samokat_logo_click(self, logo, url):
        self.click_elem_with_wait(logo)
        return self.driver.current_url.find(url) == 0

    @allure.step('Кликаем по логу Дзена')
    def main_logo_click(self, logo, url):
        original_window = self.driver.current_window_handle
        self.click_elem_with_wait(logo)
        for window_handle in self.driver.window_handles:  # для новой вкладки переключаем активное окно
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                WebDriverWait(self.driver, 5).until(
                    expected_conditions.presence_of_element_located(SwitchPageLocators.DZEN_ARCTIC))  # ждем прогрузки "статей" на дзене
                break
        return self.driver.current_url.find(url) == 0