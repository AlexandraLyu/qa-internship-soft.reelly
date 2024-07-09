from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

@given('I open the registration page')
def step_open_registration_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://soft.reelly.io/sign-up")
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "Full-Name")))

@when('I enter "{name}" as first and last name')
def step_enter_name(context, name):
    full_name_field = context.driver.find_element(By.ID, "Full-Name")
    full_name_field.send_keys(name)
    # Verify that the name was entered correctly
    assert full_name_field.get_attribute('value') == name, f"Expected name to be {name} but got {full_name_field.get_attribute('value')}"

@when('I enter "{phone}" as phone number')
def step_enter_phone(context, phone):
    phone_field = context.driver.find_element(By.ID, "phone2")
    phone_field.send_keys(phone)
    # Verify that the phone number was entered correctly
    assert phone_field.get_attribute('value') == phone, f"Expected phone to be {phone} but got {phone_field.get_attribute('value')}"

@when('I enter "{email}" as email')
def step_enter_email(context, email):
    email_field = context.driver.find_element(By.ID, "Email-3")
    email_field.send_keys(email)
    # Verify that the email was entered correctly
    assert email_field.get_attribute('value') == email, f"Expected email to be {email} but got {email_field.get_attribute('value')}"

@when('I enter "{password}" as password')
def step_enter_password(context, password):
    password_field = context.driver.find_element(By.ID, "field")
    password_field.send_keys(password)
    # Verify that the password was entered correctly
    assert password_field.get_attribute('value') == password, f"Expected password to be {password} but got {password_field.get_attribute('value')}"

@when('I enter "{company}" as company')
def step_enter_company(context, company):
    company_field = context.driver.find_element(By.ID, "Company-website")
    company_field.send_keys(company)
    # Verify that the company was entered correctly
    assert company_field.get_attribute('value') == company, f"Expected company to be {company} but got {company_field.get_attribute('value')}"

@when('I select "{role}" as role')
def step_select_role(context, role):
    role_field = Select(context.driver.find_element(By.ID, "Role"))
    role_field.select_by_visible_text(role)
    # Verify that the role was selected correctly
    selected_option = role_field.first_selected_option.text
    assert selected_option == role, f"Expected role to be {role} but got {selected_option}"

@when('I select "{country}" as country')
def step_select_country(context, country):
    country_field = Select(context.driver.find_element(By.ID, "country-select"))
    country_field.select_by_visible_text(country)
    # Verify that the country was selected correctly
    selected_option = country_field.first_selected_option.text
    assert selected_option == country, f"Expected country to be {country} but got {selected_option}"

@when('I select "{company_size}" as company size')
def step_select_company_size(context, company_size):
    company_size_field = Select(context.driver.find_element(By.ID, "Agents-amount-2"))
    company_size_field.select_by_visible_text(company_size)
    # Verify that the company size was selected correctly
    selected_option = company_size_field.first_selected_option.text
    assert selected_option == company_size, f"Expected company size to be {company_size} but got {selected_option}"

@then('the data was entered correctly')
def step_verify_data_entry(context):
    # Since verification is already done in each step, we just need to check overall completion
    pass
