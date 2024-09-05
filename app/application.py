from pages.main_page import MainPage
from pages.secondary_deals_page import SecondaryDealsPage
from pages.reelly_login_connect_company_page import ReellyLoginConnectCompanyPage
from pages.registration_page import RegistrationPage
from pages.change_password_page import ChangePasswordPage
from pages.SettingsPage import SettingsPage
from pages.LoginPage import LoginPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)
        self.secondary_deals_page = SecondaryDealsPage(driver)
        self.reelly_login_connect_company_page = ReellyLoginConnectCompanyPage(driver)
        self.registration_page = RegistrationPage(driver)
        self.change_password_page = ChangePasswordPage(driver)
        self.login_page = LoginPage(driver)
        self.settings_page = SettingsPage(driver)


