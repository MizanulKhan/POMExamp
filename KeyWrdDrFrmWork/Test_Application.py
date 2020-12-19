import pytest
import xlrd

from KeyWrdDrFrmWork.Method import Methods_List


class Test_InvalidLogin():
    def test_validate_invalide_login(self):
        workbook = xlrd.open_workbook("C:\\Users\\mizan\\Desktop\\Python&Selenium\\TestData1.xlsx")
        sheet = workbook.sheet_by_name("Sheet2")
        rowCount = sheet.nrows
        mtd= Methods_List() #call this class Method.py and make object mtd
        for i in range(1,rowCount):
            keyword = sheet.cell_value(i,3)
            if(keyword== "openBrowser"):
                mtd.openBrowser(sheet.cell_value(i,6))
            if(keyword == "maxWindow"):
                mtd.maximize_browserWindow()

            if(keyword == "impWait"):
                mtd.implicit_wait()

            if (keyword=="navigateToApp"):
                mtd.navigate_app(sheet.cell_value(i,6))

            if(keyword =="enterTextBox"):
                mtd.enterInTextBox(sheet.cell_value(i,5),sheet.cell_value(i,6))

            if(keyword =="clickButton"):
                mtd.click_button(sheet.cell_value(i,4),sheet.cell_value(i,5))

            if(keyword == "verifyMesg"):
                mtd.getErrorMesg(sheet.cell_value(i,4),sheet.cell_value(i,5))

            if(keyword=="closeApp"):
                mtd.closeBrowser()








