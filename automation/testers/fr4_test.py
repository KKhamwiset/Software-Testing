import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager


def run_fr4_test():
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
         #Searchbox
        search_xpath="//input[@placeholder='Search products...']"
        input = wait.until(EC.element_to_be_clickable((By.XPATH,search_xpath)))
        driver.execute_script("window.scrollTo(0, arguments[0].offsetTop);", input)
        time.sleep(2)
        input.clear()
        print("Sending Value")
        input.send_keys("Momentum 4")
        print("Value Sent")
        
        time.sleep(7)
        
    except Exception as e:
        print(f"Test failed: {str(e)}")