from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "deviceName": "R38M6092GWB",
    "platformName": "Android",
    "version" : "9.0",
    "appPackage": "br.com.linx.bigretail.CaixaRapido",
    "appActivity": "br.com.linx.bigretail.CaixaRapido.MainActivity",
    "realDevice": "true",
    "autoGrantPermissions": "true",
    "newCommandTimeout": "60",
    "skipDeviceInitialization": "true",
    "ignoreUnimportantViews": "true",

}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)



driver.quit()