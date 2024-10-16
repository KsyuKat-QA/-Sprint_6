from sprint_6.pages.root_page import RootPage
from sprint_6.data import *
from sprint_6.conftest import browser
import pytest
import allure

@pytest.mark.parametrize("question_num, question_ans", 
                         [(1, ANS_1),
                         (2, ANS_2),
                         (3, ANS_3),
                         (4, ANS_4),
                         (5, ANS_5),
                         (6, ANS_6),
                         (7, ANS_7),
                         (8, ANS_8)])     

@allure.title('Проверка вопрос-ответ')
@allure.description('Открываем переданный номер вопроса и сравниваем с отображаемым ответом')
def test_quesiton(browser,question_num,question_ans):
    testing_page = RootPage(browser)
    testing_page.go_to_site()
    testing_page.chavo_click(question_num)
    assert testing_page.answ_show().find(question_ans) == 0 #Ответ строго начинается с нашего шаблона