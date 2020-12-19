from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class FundTransferVerify(BasePage):
    submit_button = (By.ID,"btn_submit")

    def __init__(self, driver):
        super().__init__(driver)

    def click_submit(self):
        self.do_click(self.submit_button)