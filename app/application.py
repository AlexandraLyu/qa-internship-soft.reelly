from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage
from pages.secondary_deals_page import SecondaryDealsPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.secondary_deals_page = SecondaryDealsPage(driver)




