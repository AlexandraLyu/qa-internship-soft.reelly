from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def log_in(self, email, password):
        email_input = self.driver.find_element(By.NAME, 'email')
        password_input = self.driver.find_element(By.NAME, 'password')
        login_button = self.driver.find_element(By.XPATH, '//button[text()="Login"]')
        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def click_connect_company(self):
        try:
            connect_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'get-free-period') and contains(@class, 'menu') and text()='Connect the company']"))
            )
            connect_button.click()
        except TimeoutException:
            raise Exception("Connect the company button not clickable or not found within the expected time.")
class TabHandler:
    def __init__(self, driver):
        self.driver = driver

    def switch_to_new_tab(self):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[1])
        except TimeoutException:
            raise Exception("New tab did not open as expected.")

    def verify_tab(self, expected_title=None, expected_url=None):
        if expected_title and expected_title not in self.driver.title:
            raise AssertionError(f"Expected title '{expected_title}', but got '{self.driver.title}'")
        if expected_url and expected_url not in self.driver.current_url:
            raise AssertionError(f"Expected URL '{expected_url}', but got '{self.driver.current_url}'")

class ReellyLoginConnectCompanyPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.tab_handler = TabHandler(driver)

    def execute_scenario(self, email, password, expected_title, expected_url):
        self.login_page.log_in(email, password)
        self.dashboard_page.click_connect_company()
        self.tab_handler.switch_to.new_tab()
        self.tab_handler.verify_tab(expected_title, expected_url)
