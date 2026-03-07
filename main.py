import os
from dotenv import load_dotenv
from automation.resources import DriverManager
from automation.testers import *

def main():
    load_dotenv()
    test_list = [
        run_fr1_test,
        run_fr2_test,
        run_fr3_test
    ]
    for i in test_list:
        try:
            i()
        except:
            print(f"Test {i.__name__} failed")
            
    if DriverManager.has_instance():
        DriverManager.quit_driver()

if __name__ == "__main__":
    main()
