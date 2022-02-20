from Pages.LoginPage import basePage
from Pages.FormPage import FormPage
from behave import *
formPage=FormPage()

@given(u'Enter the environment')
def enter_enviroment(context):
    basePage.openBrowser("https://demoqa.com/text-box")

@when(u'Fill in the fields "{name}" "{email}" "{password}"')

def fill_fields(context,name,email,password):
   formPage.field_the_form(name,email,password)

@then(u'Validate entry "{name}"')
def validate_entry(context,name):
    formPage.validate_entry(name)



