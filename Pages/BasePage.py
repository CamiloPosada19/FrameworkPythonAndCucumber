import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    #-------------------------------LOCATORS-------------------------------

    #--------------------------------DRIVER----------------------------------
    option = webdriver.ChromeOptions()
    option.add_argument('ignore-certificate-errors')
    driver =""
    driver = webdriver.Chrome(executable_path=r"C:\drivers\chromedriver.exe", chrome_options=option)
    #---------------------------METODOS---------------------------------------

    def openBrowser(self,url):
        option = webdriver.ChromeOptions()
        option.add_argument('ignore-certificate-errors')
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.driver.maximize_window()
    #Click on the item with explicit wait
    def click(self, element):
        try:
            locator = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, element))
            )
            locator.click()
            print(f"the element{element}has been clicked")
        except:
            print(f"the element {element} isn't is clicked")

      # Click on the item with id
    def click_id(self, element):
        try:
            locator = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.ID, element))
            )
            locator.click()
            print(f"the element{element}has been clickKEed")
        except:
            print(f"the element {element} isn't clicked")

    def click_class(self, element):
        try:
            locator = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, element))
            )
            locator.click()
            print(f"the element{element}has been clicked")
        except:
            print(f"the element {element} isn't is displayed")




    #Write to the element with explicit wait
    def type(self,element,text):
        try:
            locator = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, element))
            )
            locator.send_keys(text)
            print(f"the text {text} has been type in the{element}")
        except:
            print(f" Could not write in the field{element}")
    #Clear fields
    def clear(self,element):
        try:
            locator = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, element))
            )
            locator.clear()
        except:
            print(f" Could not write in the field{element}")

    #Wait explicit
    def wait(self,element):
        try:
            locator = WebDriverWait(self.driver, 35).until(
                EC.visibility_of_element_located((By.XPATH, element)) )
            print(f"The element{element} is visible")
        except:
            print(f"The element{element} is not visible")
    # Validate text
    def validate_text(self,element,texto):
            element=self.driver.find_element(By.XPATH,element).text
            print(element)


            assert element==texto,"The text of the element is not the same "

    # Validate that it contains the text
    def validate_contain_text(self,element,texto):
            element = self.driver.find_element(By.XPATH, element).text
            assert texto in element,"The element NOT contains the text"
    # Validate element is visible
    def validate_element_is_visible(self,elemento):
            try:
                self.driver.find_element(By.XPATH, elemento).is_displayed()
                print(f"The element{elemento}is visible")
            except:
                print("The elements isn't is visible")
    def drag_element(self,source_element ,dest_element):
        try:
            source_element = self.driver.find_element(By.XPATH, source_element)
            dest_element = self.driver.find_element(By.XPATH, dest_element)
            ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()
            print("El elemento se desplazo")
        except:
            print("El elemento no se desplazo")



    def search_element(self,elemento):

        try:
            search=self.driver.find_element(By.XPATH,elemento)
            self.driver.execute_script('arguments[0].scrollIntoView(true);',search)
        except:
            print("No se ha desplazado ")


    def close_browser(self):
        try:
            self.driver.close()
        except:
            print("The browser didn't correctly")













