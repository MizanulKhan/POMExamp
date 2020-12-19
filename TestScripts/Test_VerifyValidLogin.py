from Pages.AccountSummary import AccountSummary
from Pages.Login import LoginPage
from TestScripts.conftest import BaseTest


class Test_VerifyLogin(BaseTest):
    def test_verify_valid_login(self):
        self.lp = LoginPage(self.driver)
        # Call this for Validation whether Transfer Fund link is exist or not
        self.acc = AccountSummary(self.driver)

#Actions
        self.lp.application_login("username","password")
        tfPresent = self.acc.isTransferfund_present()
        assert tfPresent == True
