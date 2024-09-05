class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "username").send_keys("lybchevskaya@icloud.com")
        self.driver.find_element(By.ID, "password").send_keys("Abundance88!")
        self.driver.find_element(By.ID, "login_button").click()
