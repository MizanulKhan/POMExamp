from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class FundTransferConf(BasePage):
    confar_text = (By.CSS_SELECTOR,"#transfer_funds_content > div > div > div.alert.alert-success")
    user_name = (By.CSS_SELECTOR,"#settingsBox > ul > li:nth-child(3) > a")
    log_out = (By.ID,"logout_link")
    #log_out = (By.CSS_SELECTOR,"#logout_link")

    def __init__(self, driver):
        super().__init__(driver)

    def get_confarmation_text(self):
        return self.do_getText(self.confar_text)

    def logout(self):
        self.do_click(self.user_name)
        self.do_click(self.log_out)
