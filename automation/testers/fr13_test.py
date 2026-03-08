import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait , Select
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager

def run_fr13_test():
    """Executes the FR-13 test case using the provided driver."""
    driver = DriverManager.get_driver()
    try:
       wait = WebDriverWait(driver , 10)

       # Wait for button
       print("Seeking for testing item")
       edit_testing_xpath = "//h3[normalize-space()='Testing']/ancestor::li//button[normalize-space()='Edit']"
       edit_testing_executor = wait.until(
        EC.element_to_be_clickable((By.XPATH,edit_testing_xpath))
       )
       driver.execute_script("arguments[0].scrollIntoView(true);", edit_testing_executor)
       time.sleep(0.3)
       edit_testing_executor.click()
       print("Clicked edit testing item")


       field_name= [
        ("Enter product name", "TestingEdit"),
        ("Enter brand name", "TestingEdit"),
        ("e.g. Bluetooth 5.0, 3.5mm" ,"TestingEdit"),
       ]
       for name,value in field_name:
           print(f"Waiting for {name}...")
           xpath = f"//input[@placeholder='{name}' and @required]"
           input_el = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
           input_el.clear()
           input_el.click()
           input_el.send_keys(value)
           print(f"Entered {name} successfully.")
           time.sleep(0.3) 

       # Wait for category
       print("Waiting for category...")
       option_selecter = wait.until(EC.element_to_be_clickable((By.TAG_NAME  , "select")))
       dropdown = Select(option_selecter)
       dropdown.select_by_value("1")
       time.sleep(4)
       print("Selected category successfully.")

       field_price = [
        ("Price*", "111"),
        ("Sale Price", "51"),
        ("Stock*", "1")
       ]
       for name,value in field_price:
           print(f"Waiting for {name}...")
           xpath = f"//label[normalize-space()='{name}']/following::input[1]"
           input_el = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
           input_el.clear()
           input_el.click()
           input_el.send_keys(value)
           print(f"Entered {name} successfully.")
           time.sleep(0.3) 
    

       #Textarea
       textarea_xpath = "//textarea[@required]" 
       textarea_executor = wait.until(EC.element_to_be_clickable((By.XPATH,textarea_xpath)))
       textarea_executor.clear()
       textarea_executor.click()
       textarea_executor.send_keys("TestingEdit")
       print("Clicked textarea successfully.")
       time.sleep(0.3)

       #Submit button
       submit_xpath = "//button[.//span[normalize-space()='Update Product']]"
       submit_executor = wait.until(EC.element_to_be_clickable((By.XPATH,submit_xpath)))
       submit_executor.click()
       print("Clicked update product button successfully.")
       time.sleep(0.3)
       
       updateProduct_xpath = "//h3[normalize-space()='Testing']"
       updateProduct = wait.until(EC.visibility_of_element_located((By.XPATH,updateProduct_xpath)))
       driver.execute_script("arguments[0].scrollIntoView(true);", updateProduct)
       print("Found update product")
       time.sleep(5)
    except Exception as e:
        print(f"Test failed: {str(e)}")

