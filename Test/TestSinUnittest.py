import time
from selenium import webdriver
from Pages import BasePage
from Pages.FormPage import FormPage
from Pages.LoginPage import Loginpage

basePage=BasePage.BasePage()
loginPage=Loginpage()
formPage=FormPage()


basePage.openBrowser("https://demoqa.com/text-box")
formPage.field_the_form("Camilo","camilo@camilo.com","NEA")
formPage.validate_contain_text("//div[@class='border col-md-12 col-sm-12']","CAMILO")
