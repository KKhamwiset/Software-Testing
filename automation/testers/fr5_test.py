import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager


def run_fr5_test():
    """Executes the FR-3 test case using the provided driver."""
    
    driver = DriverManager.get_driver()
    url = os.getenv("url", None)

    current_url = driver.current_url
    if url is None:
        print("URL is not provided in environment variables.")
        return
    if "product" in current_url:
        print("Already on products page.")
        driver.refresh()
        time.sleep(2)
    else:
        print(f"Navigating to {url}products")
        driver.get(url + "products")

    try:
        wait = WebDriverWait(driver, 20)
         #View Detail Button
        view_detail_xpath = "//div[contains(@class,'card')]//button"
        elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, view_detail_xpath)))
        elements = elements[0]
        elements.click()
        time.sleep(2)
        
        print("Click View Detail Succesfully")
        time.sleep(7)
        
    except Exception as e:
        print(f"Test failed: {str(e)}")