import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import get_driver

def run_fr1_test():
    """Executes the FR-1 test case using the provided driver."""
    driver = get_driver()
    url = os.getenv("url", None)
    
    if url is not None:
        print(f"Navigating to {url}login")
        driver.get(url + "login")
        
        try:
            wait = WebDriverWait(driver, 10)
            
            register_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/register']")))
            register_link.click()
            print("Successfully navigated to Register page.")

            
            fields = [
                ("firstName", "John"),
                ("lastName", "Doe"),
                ("username","JD"),
                ("email", "frtest1@gmail.com"),
                ("password", "FRtest1_123"),
                ("confirmPassword", "FRtest1_123")
            ]

            for field_id, value in fields:
                print(f"Waiting for {field_id}...")
                input_el = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
                input_el.clear()
                input_el.click()
                input_el.send_keys(value)
                print(f"Entered {field_id} successfully.")
                time.sleep(0.3) 


            print("Looking for terms checkbox...")
            term_checkbox = wait.until(EC.presence_of_element_located((By.ID, "agreeTerms")))
            driver.execute_script("arguments[0].scrollIntoView(true);", term_checkbox)
            time.sleep(0.5)
            
            if not term_checkbox.is_selected():
                driver.execute_script("arguments[0].click();", term_checkbox)
            print("Agreed to terms successfully.")

            print("Waiting for Create Account button to be enabled...")
            submit = "confirmCreation"
            
            submit_button = wait.until(EC.element_to_be_clickable((By.ID,submit)))
            wait.until(lambda d: d.find_element(By.ID, submit).is_enabled())
            
            submit_button.click()
            print("Create account button clicked successfully.")
            
            time.sleep(5)
        except Exception as e:
            print(f"Test failed: {str(e)}")
    else:
        print("URL is not provided in environment variables.")
