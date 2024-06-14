from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import logging


class MainPage(BasePage):
    EMAIL_INPUT = (By.ID, 'email-2')
    PASSWORD_INPUT = (By.ID, 'field')
    CONTINUE_BUTTON = (By.XPATH, '//a[@wized="loginButton"]')
    SECONDARY_BUTTON = (By.XPATH, '//div[text()="Secondary"]')

    def open(self, url):
        self.driver.get(url)
        sleep(2)

    def login(self, email, password):
        try:
            sleep(2)
            self.wait_for_element(By.ID, 'email-2').send_keys(email)
            logging.info(f"Email input field found and email entered: {email}")
            sleep(2)
            self.wait_for_element(By.ID, 'field').send_keys(password)
            logging.info(f"Password input field found and password entered")
            sleep(2)
            self.wait_for_element_clickable_click(By.XPATH, '//a[@wized="loginButton"]')
            logging.info("Clicked on continue button")
            sleep(2)
            current_url = self.driver.current_url
            logging.info(f"Current URL after login: {current_url}")
        except Exception as e:
            logging.error(f"Login failed: {e}")
            self.driver.save_screenshot("login_failed.png")
            raise

    def click_secondary_option(self):
        try:
            # self.wait_for_element(By.XPATH, '//a[@href="/secondary-listings"]').click()
            elements = self.find_elements(*self.SECONDARY_BUTTON)
            elements[1].click()
            current_url = self.driver.current_url
            print("current url: ", current_url)
        except Exception as e:
            print(f"Failed to click on Secondary option: {e}")
            self.driver.save_screenshot("click_secondary_option_failed.png")
