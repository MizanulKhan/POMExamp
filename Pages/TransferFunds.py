from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class TransferFunds(BasePage):
    from_Acc = (By.ID, "tf_fromAccountId")
    to_Acc = (By.ID, "tf_toAccountId")
    amount = (By.ID, "tf_amount")
    description = (By.ID,"tf_description")
    continue_button = (By.ID, "btn_submit")

    def __init__(self,driver):
        super().__init__(driver)
#Actions
    def transferFunds(self,amt,desc):
        self.select_from_dropDownIndex(self.from_Acc,2)
        self.select_from_dropDownIndex(self.to_Acc,3)
        self.do_sendKeys(self.amount,amt)
        self.do_sendKeys(self.description,desc)
        self.do_click(self.continue_button)