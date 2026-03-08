import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager


def run_fr9_10_test():
    """Executes the FR-9 test case using the provided driver."""
    
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
        
    # Check if the user is logged in
    wait_short = WebDriverWait(driver, 5)
    xpath_username = "//label[contains(@class,'btn')]"
    elem = wait_short.until(EC.presence_of_element_located((By.XPATH, xpath_username)))
    
    if elem:
        elem.click()
        logout_xpath = "//a[contains(@class,'text-red-700') and contains(text(),'Logout')]"
        logout_button = wait_short.until(EC.presence_of_element_located((By.XPATH,logout_xpath)))
        logout_button.click()
        xpath_confirm = "//span[text()='Yes, Logout']"
        con = wait_short.until(EC.presence_of_element_located((By.XPATH,xpath_confirm)))
        con.click()
        time.sleep(5)
        driver.refresh()
        driver.get(url + "products/headphones/6")


    # Click Add to Cart Button
    try:
        print("Doing main task")
        wait = WebDriverWait(driver, 30)
        add_to_cart_xpath = "//button[text()=' Add to Cart']"
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
        add_btn.click()
        
        print("Click Add to Cart Successfully")

        
        time.sleep(5)
        
    except Exception as e:
        print(f"Test failed: {str(e)}")