import pytest
from selenium import webdriver
from Config.Configuration import TestData


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
    request.cls.driver = web_driver
    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    web_driver.implicitly_wait(30)

    yield
    web_driver.close()

@pytest.mark.usefixtures("init_driver")

class BaseTest:
    pass

