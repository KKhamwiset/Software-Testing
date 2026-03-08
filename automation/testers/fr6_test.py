import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager


def run_fr6_test():
    """Executes the FR-6 test case using the provided driver."""
    
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
        print(f"Navigating to {url}products/headphones/6")
        driver.get(url + "products/headphones/6")

    try:
        wait = WebDriverWait(driver, 20)
         #Add to Cart Button
        add_to_cart_xpath = "//button[text()=' Add to Cart']"
        elements = wait.until(EC.presence_of_element_located((By.XPATH, add_to_cart_xpath)))
        elements.click()
        time.sleep(2)
        
        print("Click Add to Cart Succesfully")
        time.sleep(7)
        
    except Exception as e:
        print(f"Test failed: {str(e)}")