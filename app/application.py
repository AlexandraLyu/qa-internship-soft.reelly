from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.secondary_deals_page import SecondaryDealsPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.secondary_deals_page = SecondaryDealsPage(self.driver)

    def quit(self):
        self.driver.quit()
