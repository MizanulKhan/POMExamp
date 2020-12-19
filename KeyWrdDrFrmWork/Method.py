from selenium import webdriver




class Methods_List:
    driver = None
    def openBrowser(self,driverPath):
        global driver
        self.driver = webdriver.Chrome(executable_path=driverPath)

    def maximize_browserWindow(self):
        self.driver.maximize_window()

    def implicit_wait(self):
        self.driver.implicitly_wait(30)

    def navigate_app(self,url):
        self.driver.get(url)

    def enterInTextBox(self,locValue,testData):
        self.driver.find_element_by_id(locValue).send_keys(testData)

    def click_button(self,loc,locValue):
        if(loc =="name"):
            self.driver.find_element_by_name(locValue).click()
        if(loc =="cssSelector"):#if(loc == "xpath"):
            self.driver.find_element_by_css_selector(locValue).click()
            #self.driver.find_element_by_xpath(locValue).click()

    def getErrorMesg(self,loc,locValue):
        erroMsg = None
        if(loc =="cssSelector"):
            erroMsg= self.driver.find_element_by_css_selector(locValue).text
        if(loc == "id"):
            erroMsg =self.driver.find_element_by_id(locValue).text

        return erroMsg

    def closeBrowser(self):
        self.driver.close()


