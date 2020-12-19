from Pages.Login import LoginPage
from TestScripts.conftest import BaseTest


class Test_VerifyInvalidLogin(BaseTest):
    def test_invalidLogin(self):
        self.lp = LoginPage(self.driver)

        self.lp.application_login("username11","password1")
        error_messgae = self.lp.get_errMsg()
        assert error_messgae == "Login and/or password are wrong."

