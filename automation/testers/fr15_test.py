from .fr2_test import run_fr2_test
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait , Select
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager
import time , os

def run_fr15_test():
    """Executes the FR-15 test case using the provided driver."""
    driver = DriverManager.get_driver()
    url = os.getenv("url")
    try:
       wait = WebDriverWait(driver , 10)

       # Wait for button
       print("Seeking for logout button")
       logout_xpath = "//button[normalize-space()='Logout']"
       logout_executor = wait.until(
        EC.element_to_be_clickable((By.XPATH,logout_xpath))
       )
       time.sleep(0.3)
       logout_executor.click()
       print("Clicked logout button successfully.")

       time.sleep(5)

       #Log in via user acc
       run_fr2_test()

       #Direct access to admin route
       time.sleep(5)
       driver.get(url + "admin")
       print("Testing admin route")
       admin_header_xpath = "//header//h2[normalize-space()='Admin Panel']"
       try:
        wait.until(EC.visibility_of_element_located((By.XPATH,admin_header_xpath)))
        print("Test failed admin route accessed succesfully")
       except:
        print("Cannot access admin route , test succeed")
       time.sleep(5)
       
    except Exception as e:
        print(f"Test failed: {str(e)}")