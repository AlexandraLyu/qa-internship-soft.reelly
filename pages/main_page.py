
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input.input.w-input[name="email-2"][type="email"][id="email-2"]')
    PASSWORD_INPUT = (By.ID, 'field')
    CONTINUE_BUTTON = (By.XPATH, '//a[@class="login-button w-button" and text()="Continue"]')

    def open(self, url):
        self.driver.get(url)

    def login(self, email, password):
        self.wait_for_element(By.ID, 'email-2').send_keys(email)
        self.wait_for_element(By.ID, 'field').send_keys(password)
        self.wait_for_element(By.CLASS_NAME, 'login-button').click()

    def click_secondary_option(self):
        self.wait_for_element(By.LINK_TEXT, 'Secondary').click()
