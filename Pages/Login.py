from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class LoginPage(BasePage):
    user_name = (By.ID,"user_login")
    user_password = (By.ID,"user_password")
    sign_in = (By.NAME,"submit")
    err_msg = (By.CSS_SELECTOR,"#login_form > div.alert.alert-error")

    def __init__(self,driver):
        super().__init__(driver)

#Actions
    def application_login(self,loginName,loginPassword):
        self.do_sendKeys(self.user_name, loginName)
        self.do_sendKeys(self.user_password,loginPassword)
        self.do_click(self.sign_in)

    def get_errMsg(self):
        err_msg = self.do_getText(self.err_msg)
        return err_msg