from sprint_6.locators.switch_locators import SwitchPageLocators
from sprint_6.pages.switch_page import SwitchPage
from sprint_6.conftest import browser
from sprint_6.data import *
import allure

@allure.title('Лого самоката')
@allure.description('Проверяем переход по клику через логотип самоката (попадаем на главную)')
@allure.link(ROOT_URL, name='Главная ссылка самоката')
def test_logo_samokat(browser):
    testing_page = SwitchPage(browser)
    testing_page.go_to_site()
    assert testing_page.samokat_logo_click(SwitchPageLocators.SAMOKAT_LOGO, ROOT_URL)

@allure.title('Лого Дзена')
@allure.description('Проверяем переход по клику через логотип Дзена')
@allure.link(DZEN_URL, name='Главная ссылка Дзена')
def test_logo_dzen(browser):
    testing_page = SwitchPage(browser)
    testing_page.go_to_site()
    assert testing_page.main_logo_click(SwitchPageLocators.MAIN_LOGO, DZEN_URL)