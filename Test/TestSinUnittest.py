import time
from selenium import webdriver
from Pages import BasePage
from Pages.LoginPage import Loginpage

basePage=BasePage.BasePage()
loginPage=Loginpage()


basePage.openBrowser("https://demoqa.com/text-box")
