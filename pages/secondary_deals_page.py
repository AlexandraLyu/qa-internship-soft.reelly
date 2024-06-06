import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import logging
from .base_page import BasePage

class SecondaryDealsPage(BasePage):
    def verify_on_page(self, expected_url):
        """
        Verify the current URL is the expected URL for the Secondary deals page.
        """
        try:
            self.wait.until(EC.url_to_be(expected_url))
            assert self.driver.current_url == expected_url, f"Expected URL to be {expected_url} but got {self.driver.current_url}"
        except TimeoutException:
            current_url = self.driver.current_url
            logging.error(f"Failed to navigate to URL: {expected_url}, current URL: {current_url}")
            self.driver.save_screenshot("url_verification_failed.png")
            raise

    def filter_by_want_to_sell(self):
        """
        Apply the 'want to sell' filter on the Secondary deals page.
        """
        try:
            # Click on the Filters button
            filters_button = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='filter-button']")))
            print(f"Filters button found: {filters_button}")
            filters_button.click()

            # Wait until the 'Want to sell' option is clickable
            want_to_sell_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Want to sell']")))

            # Add a short delay to ensure stability
            time.sleep(1)

            # Click on the 'Want to sell' option
            want_to_sell_option.click()

            # Scroll down to locate the 'Apply filter' button
            apply_filter_button = self.wait_for_element(By.XPATH, "//a[@wized='applyFilterButtonMLS' and text()='Apply filter']")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", apply_filter_button)

            # Ensure the button is visible and interactable before clicking
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@wized='applyFilterButtonMLS' and text()='Apply filter']")))

            # Click on the 'Apply filter' button using JavaScript if necessary
            try:
                apply_filter_button.click()
            except ElementNotInteractableException:
                logging.warning("Element not interactable via normal click, using JavaScript click.")
                self.driver.execute_script("arguments[0].click();", apply_filter_button)
        except ElementNotInteractableException as e:
            logging.error("Element not interactable: Apply filter button.")
            self.driver.save_screenshot("apply_filter_not_interactable.png")
            raise e

    def verify_all_cards_have_for_sale_tag(self):
        """
        Verify all displayed cards have a 'for sale' tag.
        """
        try:
            # Scroll down the page to load all cards
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)  # wait for new elements to load
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            cards = self.wait_for_elements(By.CSS_SELECTOR, 'div[wized="listingCardMLS"]')
            for card in cards:
                tag_element = card.find_element(By.XPATH, ".//div[@wized='saleTagMLS']")
                assert tag_element.text == 'For sale', f"Expected 'For sale' tag but got {tag_element.text}"
        except TimeoutException:
            logging.error("Elements not found: div[wized='listingCardMLS']")
            self.driver.save_screenshot("cards_not_found.png")
            raise
