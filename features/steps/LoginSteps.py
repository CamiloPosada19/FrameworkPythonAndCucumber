from behave import *
from cucumber_tag_expressions.model import And

from Pages.BasePage import BasePage
from Pages.LoginPage import Loginpage

basePage=BasePage()
loginPage=Loginpage()

@given(u'Open the browser')
def open_browser(context):
    basePage.openBrowser("https://demoqa.com/login")
    print("Prueba")

@when(u'Enter an incorrect login')
def enter_login_incorrect(context):
    loginPage.makeLogin("loginIncorrect","123")
    print("Prueba")

@when(u'Verify validation of incorrect login')
def verify_login_incorrect(context):
    loginPage.verifyValidationIncorrect()

@then(u'Close the browser')
def close_browser(context):
    #basePage.close_browser()
    print("Prueba")

#------------------------Login correct------------

@when(u'Clear fields')
def clear_fields(context):
    loginPage.clear_fields()

@when(u'Make a login correctly and validate login')
def make_login_and_verify(context):
    loginPage.makeLogin("testtest","Test123!")
    loginPage.verifyValidationLoginCorrect("testtest")