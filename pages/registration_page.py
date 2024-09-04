from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://soft.reelly.io/sign-up"

    def open(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "Full-Name")))

    def enter_name(self, name):
        full_name_field = self.driver.find_element(By.ID, "Full-Name")
        full_name_field.send_keys(name)
        return full_name_field.get_attribute('value') == name

    def enter_phone(self, phone):
        phone_field = self.driver.find_element(By.ID, "phone2")
        phone_field.send_keys(phone)
        return phone_field.get_attribute('value') == phone

    def enter_email(self, email):
        email_field = self.driver.find_element(By.ID, "Email-3")
        email_field.send_keys(email)
        return email_field.get_attribute('value') == email

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "field")
        password_field.send_keys(password)
        return password_field.get_attribute('value') == password

    def enter_company(self, company):
        company_field = self.driver.find_element(By.ID, "Company-website")
        company_field.send_keys(company)
        return company_field.get_attribute('value') == company

    def select_role(self, role):
        role_field = Select(self.driver.find_element(By.ID, "Role"))
        role_field.select_by_visible_text(role)
        return role_field.first_selected_option.text == role

    def select_country(self, country):
        country_field = Select(self.driver.find_element(By.ID, "country-select"))
        country_field.select_by_visible_text(country)
        return country_field.first_selected_option.text == country

    def select_company_size(self, company_size):
        company_size_field = Select(self.driver.find_element(By.ID, "Agents-amount-2"))
        company_size_field.select_by_visible_text(company_size)
        return company_size_field.first_selected_option.text == company_size
