import time

from Pages.BasePage import BasePage


class FormPage(BasePage):
    #Locators
    inpt_name_xpath="//input[@placeholder='Full Name']"
    inpt_email_xpath="//input[contains(@type,'email')]"
    inpt_address_xpath="//textarea[contains(@placeholder,'Current Address')]"
    btn_submit_xpath="//button[contains(@class,'btn btn-primary')]"
    text_validation_xpath="//div[@class='border col-md-12 col-sm-12']"


    def field_the_form(self,name,email,address):
        #self.search_element(self.btn_submit_xpath)
        self.type(self.inpt_name_xpath,name)
        self.type(self.inpt_email_xpath,email)
        self.type(self.inpt_address_xpath,address)
        time.sleep(2)
        self.click_id("submit")


    def validate_entry(self,texto):
        self.validate_contain_text(self.text_validation_xpath,texto)
