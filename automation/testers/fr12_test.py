import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait , Select
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager

def run_fr12_test():
    """Executes the FR-12 test case using the provided driver."""
    driver = DriverManager.get_driver()
    try:
       wait = WebDriverWait(driver , 10)

       # Wait for button
       print("Seeking for product button")
       product_css = "a[href='/admin/products']"
       product_css_executor = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,product_css))
       )
       product_css_executor.click()
       print("Clicked product button")

       # Wait for add product
       print("Seeking for add product button")
       add_product_xpath = "//button[normalize-space()='Add Product']"
       add_product_css_executor = wait.until(
        EC.element_to_be_clickable((By.XPATH,add_product_xpath))
       )
       add_product_css_executor.click()
       print("Clicked add product button")

       field_name= [
        ("Enter product name", "Testing"),
        ("Enter brand name", "Testing"),
        ("e.g. Bluetooth 5.0, 3.5mm" ,"Testing"),
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
        ("Price*", "100"),
        ("Sale Price", "50"),
        ("Stock*", "2")
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
       textarea_executor.send_keys("Testing")
       print("Clicked textarea successfully.")
       time.sleep(0.3)

       #Submit button
       submit_xpath = "//button[.//span[normalize-space()='Create Product']]"
       submit_executor = wait.until(EC.element_to_be_clickable((By.XPATH,submit_xpath)))
       submit_executor.click()
       print("Clicked submit button successfully.")
       time.sleep(0.3)
       
       time.sleep(5)
    except Exception as e:
        print(f"Test failed: {str(e)}")

