import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

def get_driver():
    """Initializes and returns an Edge WebDriver instance."""
    # Resolve path relative to this file (automation/resources/driver.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Binary is in automation/resources/edgedriver_win64/msedgedriver.exe
    driver_path = os.path.join(current_dir, "edgedriver_win64", "msedgedriver.exe")
    
    service = Service(executable_path=driver_path) 
    driver = webdriver.Edge(service=service)
    return driver
