import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager

def run_fr2_test():
    """Executes the FR-2 test case using the provided driver."""
    driver = DriverManager.get_driver()
    url = os.getenv("url", None)
    
    if url is not None and  "login" not in driver.current_url:
        print(f"Navigating to {url}login")
        driver.get(url + "login")
        
    try:
        wait = WebDriverWait(driver, 15)
        user = os.getenv("JD")
        passwd = os.getenv("FRtest1_123")
        field =[
            ("user_email", user),
            ("password" , passwd),
        ]
        for id,value in field:
            print(f"Waiting for {id}...")
            input_el = wait.until(EC.visibility_of_element_located((By.ID, id)))
            input_el.clear()
            input_el.click()
            input_el.send_keys(value)
            print(f"Entered {id} successfully.")
            time.sleep(0.3) 
        id = "login"
        log_in_button = wait.until(EC.element_to_be_clickable((By.ID, id)))
        wait.until(lambda d: d.find_element(By.ID, id).is_enabled())
        log_in_button.click()
        print("Log in succesfully")
        time.sleep(2)
        
    except Exception as e:
        print(f"Test failed: {str(e)}")
    else:
        print("URL is not provided in environment variables.")
