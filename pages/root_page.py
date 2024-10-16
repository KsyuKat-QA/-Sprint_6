from sprint_6.pages.base_page import BasePage
from sprint_6.locators.root_page_locators import RootPageLocators
from selenium.webdriver.common.by import By
import allure
from sprint_6.data import *

class RootPage(BasePage):
    @allure.step('Открыли браузер по ссылке ' + ROOT_URL)
    def go_to_site(self):
        self.driver.get(ROOT_URL)
        self.click_elem_with_wait(RootPageLocators.BUT_COOKIE)  # соглашаемся на куки
        return self.driver

    @allure.step('Открыли номер вопроса')
    def chavo_click(self, question_num):
        block = self.find_elems_with_wait(RootPageLocators.QUESTIONS_BLOCK)
        block[question_num - 1].click()  # из массива вопросов кликаем по нужному

    @allure.step('Вернули текст отображаеого ответа')
    def answ_show(self):  # идем по всем ответам, возвращаем тот который отображается

        block = self.find_elems_with_wait(RootPageLocators.ANS_BLOCK)
        for elem in block:
            if elem.find_element(By.TAG_NAME, "p").is_displayed():
                answ = elem.find_element(By.TAG_NAME, "p").text
                break
        return answ