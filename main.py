import os,sys
from dotenv import load_dotenv
from automation.resources import DriverManager
from automation.testers import *

def main():
    load_dotenv()
    test_list = [
        run_fr1_test,
        run_fr2_test,
        run_fr3_test,
        run_fr4_test,
        run_fr5_test,
        run_fr6_test,
        run_fr7_test,
        run_fr8_test,
        run_fr9_10_test,
        run_fr11_test,
        run_fr12_test
    ]
    selected_test = sys.argv[1::] if len(sys.argv) > 1 else None
    for test in test_list:
        try:
            if selected_test and test.__name__ not in selected_test:
                continue

            print(f"Running {test.__name__}")
            test()

        except Exception as e:
            print(f"Test {test.__name__} failed: {e}")
            
    if DriverManager.has_instance():
        DriverManager.quit_driver()

if __name__ == "__main__":
    main()
