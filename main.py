import os
from dotenv import load_dotenv
from automation.resources import get_driver
from automation.testers import *

def main():
    load_dotenv()
    driver = get_driver()
    test_list = [
        run_fr1_test,
        run_fr2_test
    ]
    for i in test_list:
        try:
            i()
        except:
            print(f"Test {i.__name__} failed")
        finally:
            driver.quit()

if __name__ == "__main__":
    main()
