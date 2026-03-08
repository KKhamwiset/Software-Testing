import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait , Select
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager

def run_fr14_test():
    """Executes the FR-14 test case using the provided driver."""
    driver = DriverManager.get_driver()
    try:
       wait = WebDriverWait(driver , 10)

       # Wait for button
       print("Seeking for testing item")
       edit_testing_xpath = "//h3[normalize-space()='TestingEdit']/ancestor::li//button[normalize-space()='Delete']"
       edit_testing_executor = wait.until(
        EC.element_to_be_clickable((By.XPATH,edit_testing_xpath))
       )
       driver.execute_script("arguments[0].scrollIntoView(true);", edit_testing_executor)
       time.sleep(0.3)
       edit_testing_executor.click()
       print("Clicked Deleting testing edit item")

       #Delete button
       delete_xpath = "//div[contains(@class,'modal')]//button[normalize-space()='Delete']"
       delete_executor = wait.until(EC.element_to_be_clickable((By.XPATH,delete_xpath)))
       delete_executor.click()
       print("Clicked confirm delete product button successfully.")
       time.sleep(5)
    except Exception as e:
        print(f"Test failed: {str(e)}")

