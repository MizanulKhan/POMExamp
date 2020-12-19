
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator)).click()

    def do_sendKeys(self,by_locator,value):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator)).send_keys(value)

    def do_getText(self,by_locator):
        el = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        return el.text

    def isElement_Present(self,by_locator):
        el= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        return el.is_displayed()

    def select_from_dropDownIndex(self,by_locator,value_index):
        el = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        dd = Select(el)
        dd.select_by_index(value_index)




