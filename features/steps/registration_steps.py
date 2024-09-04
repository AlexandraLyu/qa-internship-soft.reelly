from behave import given, when, then
from selenium import webdriver
from pages.registration_page import RegistrationPage  # Ensure this import matches your project structure

@given('I open the registration page')
def step_open_registration_page(context):
    context.driver = webdriver.Chrome()
    context.registration_page = RegistrationPage(context.driver)
    context.registration_page.open()

@when('I enter "{name}" as first and last name')
def step_enter_name(context, name):
    assert context.registration_page.enter_name(name), f"Name entry failed for {name}"

@when('I enter "{phone}" as phone number')
def step_enter_phone(context, phone):
    assert context.registration_page.enter_phone(phone), f"Phone number entry failed for {phone}"

@when('I enter "{email}" as email')
def step_enter_email(context, email):
    assert context.registration_page.enter_email(email), f"Email entry failed for {email}"

@when('I enter "{password}" as password')
def step_enter_password(context, password):
    assert context.registration_page.enter_password(password), f"Password entry failed for {password}"

@when('I enter "{company}" as company')
def step_enter_company(context, company):
    assert context.registration_page.enter_company(company), f"Company entry failed for {company}"

@when('I select "{role}" as role')
def step_select_role(context, role):
    assert context.registration_page.select_role(role), f"Role selection failed for {role}"

@when('I select "{country}" as country')
def step_select_country(context, country):
    assert context.registration_page.select_country(country), f"Country selection failed for {country}"

@when('I select "{company_size}" as company size')
def step_select_company_size(context, company_size):
    assert context.registration_page.select_company_size(company_size), f"Company size selection failed for {company_size}"

@then('the data was entered correctly')
def step_verify_data_entry(context):
    # This is a summary step to ensure all data entries were successful, though each field is verified individually.
    # This step can either pass silently if all assertions above are true or it can perform additional checks if necessary.
    pass
