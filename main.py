import os
from dotenv import load_dotenv
from automation.resources import get_driver
from automation.testers import run_fr1_test

def main():
    load_dotenv()
    driver = get_driver()
    test_list = [
        run_fr1_test
    ]
    for i in test_list:
        try:
            i()
        except:
            print(f"Test {i.__name__} failed")
    if driver:
        driver.quit()

if __name__ == "__main__":
    main()
