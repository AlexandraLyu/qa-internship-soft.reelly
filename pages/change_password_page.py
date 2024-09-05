class ChangePasswordPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_change_password_page(self):
        # This can be improved with more specific checks
        return "Change Your Password" in self.driver.title

    def enter_new_password(self, new_password):
        self.driver.find_element(By.ID, "new_password").send_keys(new_password)
        self.driver.find_element(By.ID, "confirm_new_password").send_keys(new_password)

    def verify_change_password_button_enabled(self):
        return self.driver.find_element(By.ID, "submit_button").is_enabled()
