import os
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

EVID_DIR = "evidencias"
os.makedirs(EVID_DIR, exist_ok=True)

def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def screenshot(driver, name):
    safe_name = re.sub(r"[^a-z0-9_-]+", "_", name.lower())
    driver.save_screenshot(f"{EVID_DIR}/{int(time.time())}_{safe_name}.png")

