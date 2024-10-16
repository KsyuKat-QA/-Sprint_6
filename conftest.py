from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    ff_options = webdriver.FirefoxOptions()
    # ff_options.add_argument('--headless') # добавили настройку
    ff_options.add_argument('--window-size=1550,1000')  # добавили ещё настройку
    driver = webdriver.Firefox(options=ff_options)

    yield driver
    driver.quit()