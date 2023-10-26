from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

options = webdriver.FirefoxOptions()
options.set_preference("detach", True)
service_obj = Service("C:\\Users\\nikit\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver.exe")
driver = webdriver.Firefox(options=options)
driver.get("https://www.amazon.com/")