import xlrd

from Config.Configuration import TestData
from Pages.AccountSummary import AccountSummary
from Pages.FundTransfer import FundTransferVerify
from Pages.FundTransferConfarmation import FundTransferConf
from Pages.Login import LoginPage
from Pages.TransferFunds import TransferFunds
from TestScripts.conftest import BaseTest


class Test_fundTransfer(BaseTest):
    def test_VerifyFundTransfer(self):
        self.lf = LoginPage(self.driver)
        self.acc = AccountSummary(self.driver)
        self.tf = TransferFunds(self.driver)
        self.tfv = FundTransferVerify(self.driver)
        self.tfc = FundTransferConf(self.driver)

        #Take the Data from XL sheet
        workbook = xlrd.open_workbook("C:\\Users\\mizan\\Desktop\\Python&Selenium\\TestData1.xlsx")
        sheet = workbook.sheet_by_name("Sheet1")
        rowCount = sheet.nrows

        for i in range(1,rowCount):
            uName = sheet.cell_value(i,0)
            passWord = sheet.cell_value(i,1)
            amt = sheet.cell_value(i,2)
            desc = sheet.cell_value(i,3)
            expectedMesg = sheet.cell_value(i,4)

            self.lf.application_login(uName,passWord)
            self.acc.click_TransferFunds()
            self.tf.transferFunds(amt,desc)
            self.tfv.click_submit()
            actualMsg = self.tfc.get_confarmation_text()
            assert actualMsg == expectedMesg
            self.tfc.logout()
            self.driver.get(TestData.BASE_URL)

