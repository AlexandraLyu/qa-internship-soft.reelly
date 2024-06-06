from pages.main_page import MainPage
from pages.secondary_deals_page import SecondaryDealsPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.secondary_deals_page = SecondaryDealsPage(driver)




