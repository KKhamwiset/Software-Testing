import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.resources import DriverManager


def click_filter(wait, text):
    """Clicks a filter checkbox by label text."""
    xpath = f"//label[.//span[text()='{text}']]"
    label = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    label.click()
    print(f"Selected {text} successfully.")


def run_fr3_test():
    """Executes the FR-3 test case using the provided driver."""
    
    driver = DriverManager.get_driver()
    url = os.getenv("url", None)

    if url is None:
        print("URL is not provided in environment variables.")
        return

    print(f"Navigating to {url}products")
    driver.get(url + "products")

    try:
        wait = WebDriverWait(driver, 15)

        # Brand
        click_filter(wait, "Sennheiser")
        time.sleep(2)

        # Connectivity
        click_filter(wait, "3.5mm")
        time.sleep(2)

        click_filter(wait, "Bluetooth")
        time.sleep(2)

        # Price
        click_filter(wait, "$100 - $300")
        time.sleep(4)

        product_figures_xpath = "//div[contains(@class,'card')]/figure"
        figures = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, product_figures_xpath))
        )

        print(f"\nProducts found: {len(figures)}\n")

        for fig in figures:
            card = fig.find_element(By.XPATH, "..") 

            name = card.find_element(
                By.XPATH,
                ".//h2[contains(@class,'text-lg')]"
            ).text

            brand = card.find_element(
                By.XPATH,
                ".//h2[contains(@class,'text-primary')]"
            ).text

            print(f"{brand} - {name}")
    except Exception as e:
        print(f"Test failed: {str(e)}")