from selenium.webdriver.common.by import By  # Import the By class from Selenium

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_settings(self):
        self.driver.find_element(By.ID, "settings_menu").click()

    def change_password(self):
        self.driver.find_element(By.ID, "change_password_option").click()
