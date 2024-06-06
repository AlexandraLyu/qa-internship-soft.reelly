import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)  # Increased wait time

    def wait_for_element(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            logging.info(f"Element found: {by}={value}")
            return element
        except TimeoutException:
            logging.error(f"Element not found: {by}={value}")
            self.driver.save_screenshot("element_not_found.png")
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise

    def wait_for_element_clickable_click(self, by, value):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            logging.info(f"Element found: {by}={value}")
            return element.click()
        except TimeoutException:
            logging.error(f"Element not found: {by}={value}")
            self.driver.save_screenshot("element_not_found.png")
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise

    def wait_for_elements(self, by, value):
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located((by, value)))
            logging.info(f"Elements found: {by}={value}")
            return elements
        except TimeoutException:
            logging.error(f"Elements not found: {by}={value}")
            self.driver.save_screenshot("elements_not_found.png")
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            raise
