import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.BasePage import BasePage
from selenium.webdriver import ActionChains

import unittest

basePage=BasePage()
class Loginpage(BasePage):
    #Locators
    __inputUserXpath="//input[contains(@placeholder,'UserName')]"
    __inputPasswordXpath="//input[@placeholder='Password']"
    __btonLoginXpath="//button[@type='button'][contains(.,'Login')]"
    __textValidation="//p[@class='mb-1'][contains(.,'Invalid username or password!')]"
    __textValidationLoginCorrectly="//label[@class='form-label'][contains(.,'testtest')]"


    def makeLogin(self,user,password):
        self.type(self.__inputUserXpath,user)
        self.type(self.__inputPasswordXpath,password)
        self.click(self.__btonLoginXpath)

    def verifyValidationIncorrect (self):
        self.validate_text(self.__textValidation,"Invalid username or password!")
        self.validate_element_is_visible(self.__textValidation)

    def verifyValidationLoginCorrect(self,texto):
        self.validate_text(self.__textValidationLoginCorrectly,texto)

    def clear_fields(self):
        self.clear(self.__inputUserXpath)
        self.clear(self.__inputPasswordXpath)









