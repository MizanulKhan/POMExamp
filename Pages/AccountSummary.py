from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AccountSummary(BasePage):
    TransferFunds = (By.LINK_TEXT, "Transfer Funds")

    def __init__(self, driver):
        super().__init__(driver)

    def click_TransferFunds(self):
        self.do_click(self.TransferFunds)

#it will check the Account Summary page's link Transfer Fund present or not
    def isTransferfund_present(self):
        isTFPresent= self.isElement_Present(self.TransferFunds)
        return isTFPresent

