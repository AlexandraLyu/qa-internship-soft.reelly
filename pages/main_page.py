from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input.input.w-input[name="email-2"][type="email"][id="email-2"]')
    PASSWORD_INPUT = (By.ID, 'field')
    CONTINUE_BUTTON = (By.XPATH, '//a[@class="login-button w-button" and text()="Continue"]')

    def open(self, url):
        self.driver.get(url)
        sleep(2)

    def login(self, email, password):
        sleep(2)
        self.wait_for_element(By.ID, 'email-2').send_keys(email)
        sleep(2)
        self.wait_for_element(By.ID, 'field').send_keys(password)
        sleep(2)
        self.wait_for_element_clickable_click(By.CLASS_NAME, 'login-button')

    def click_secondary_option(self):
        self.wait_for_element(By.XPATH, '//a[@href="/secondary-listings"]').click()
        current_url = self.driver.current_url
        print("current url: ", current_url)
