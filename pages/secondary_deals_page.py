from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
import logging
from .base_page import BasePage
import time

class SecondaryDealsPage(BasePage):
    SECONDARY_OPTION = (By.CSS_SELECTOR, "a.menu-project.open.w--current[href='/secondary-listings'][aria-current='page']")

    def verify_on_page(self):
        try:
            time.sleep(20)  # Adding a sleep to wait for the page to fully load
            self.wait_for_element(*self.SECONDARY_OPTION)
            logging.info(f"Successfully found the secondary deals element.")
        except TimeoutException:
            logging.error(f"Failed to find the secondary deals element.")
            self.driver.save_screenshot("element_verification_failed.png")
            with open("page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            logs = self.driver.get_log('browser')
            with open("console.log", "w") as log_file:
                for entry in logs:
                    log_file.write(f"{entry['level']}: {entry['message']}\n")
            raise

    def filter_by_want_to_sell(self):
        try:
            self.wait_for_element(By.XPATH, "//div[text()='Filters']").click()
            logging.info("Clicked on the Filters button.")

            want_to_sell_option = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Want to sell']"))
            )
            logging.info("Found 'Want to sell' option.")

            want_to_sell_option.click()
            logging.info("Clicked on the 'Want to sell' option.")

            apply_filter_button = self.wait_for_element(By.XPATH,
                                                        "//a[@wized='applyFilterButtonMLS' and text()='Apply filter']")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", apply_filter_button)
            logging.info("Scrolled to 'Apply filter' button.")

            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@wized='applyFilterButtonMLS' and text()='Apply filter']"))
            )

            try:
                apply_filter_button.click()
                logging.info("Clicked on the 'Apply filter' button.")
            except ElementNotInteractableException:
                logging.warning("Element not interactable via normal click, using JavaScript click.")
                self.driver.execute_script("arguments[0].click();", apply_filter_button)
        except ElementNotInteractableException as e:
            logging.error("Element not interactable: Apply filter button.")
            self.driver.save_screenshot("apply_filter_not_interactable.png")
            raise e

    def verify_all_cards_have_for_sale_tag(self):
        try:
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[wized="listingCardMLS"]')))
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            logging.info("Scrolled to the bottom of the page to load all cards.")

            cards = self.wait_for_elements(By.CSS_SELECTOR, 'div[wized="listingCardMLS"]')
            logging.info(f"Found {len(cards)} cards on the page.")
            for card in cards:
                tag_element = card.find_element(By.XPATH, ".//div[@wized='saleTagMLS']")
                assert tag_element.text == 'For sale', f"Expected 'For sale' tag but got {tag_element.text}"
            logging.info("All cards have 'For sale' tags.")
        except TimeoutException:
            logging.error("Elements not found: div[wized='listingCardMLS']")
            self.driver.save_screenshot("cards_not_found.png")
            raise
