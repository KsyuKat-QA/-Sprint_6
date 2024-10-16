from sprint_6.pages.order_page import OrderPage
from sprint_6.conftest import browser
from sprint_6.data import *
import pytest
import allure

@allure.title('Заказ самоката')
@allure.description('На странице вводим регистрационные данные и заказываем самокат')
@pytest.mark.parametrize("name,famil,addres,metro,mobile,time,duration",
                         [([*reg_data_param_set_1]),
                         ([*reg_data_param_set_2])])
def test_fill_reg_data(browser,name,famil,addres,metro,mobile,time,duration):
    testing_page = OrderPage(browser)
    testing_page.go_to_site()
    testing_page.fill_name(name)
    testing_page.fill_famil(famil)
    testing_page.fill_addres(addres)
    testing_page.fill_metro(metro)
    testing_page.fill_mobile(mobile)
    testing_page.go_but_next()

    testing_page.fill_time(time)
    testing_page.fill_duration(duration)
    testing_page.fill_color()
    testing_page.go_but_order()

    testing_page.go_confirm()

    assert testing_page.is_order_done()