import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service


class DriverManager:
    _driver = None 

    @classmethod
    def get_driver(cls):
        """Return existing driver or create a new one."""
        if cls._driver is None:
            print("Creating new Edge driver instance...")

            current_dir = os.path.dirname(os.path.abspath(__file__))
            driver_path = os.path.join(
                current_dir,
                "edgedriver_win64",
                "msedgedriver.exe"
            )

            service = Service(executable_path=driver_path)
            cls._driver = webdriver.Edge(service=service)
            cls._driver.maximize_window()
            cls._driver.set_page_load_timeout(10)

        else:
            print("Reusing existing driver instance...")

        return cls._driver

    @classmethod
    def has_instance(cls):
        """Check if driver instance already exists."""
        return cls._driver is not None

    @classmethod
    def quit_driver(cls):
        """Close driver safely."""
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
            print("Driver closed.")