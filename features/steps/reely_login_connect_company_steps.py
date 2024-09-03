from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.reelly_login_connect_company_page import ReellyLoginConnectCompanyPage

@given('I am on the Reelly sign-up page')
def step_impl_given_user_on_signup_page(context):
    # Initialize the Chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.get("https://soft.reelly.io/sign-up")
    # Initialize the page object
    context.reelly_page = ReellyLoginConnectCompanyPage(context.driver)

@when('I log in with the email "{email}" and password "{password}"')
def step_impl_when_user_logs_in(context, email, password):
    # Step 1: Click on the sign in button
    sign_in_button = context.driver.find_element(By.XPATH, "//div[@wized='signinButtonSignup' and @class='sing-in-text' and text()='Sign in']")
    sign_in_button.click()
    # Step 2: Input email
    email_field = context.driver.find_element(By.CSS_SELECTOR, "input#email-2")
    email_field.clear()
    email_field.send_keys(email)
    # Step 3: Input password
    password_field = context.driver.find_element(By.CSS_SELECTOR, "input#field")
    password_field.clear()
    password_field.send_keys(password)
    # Step 4: Click on continue
    continue_button = context.driver.find_element(By.CSS_SELECTOR, "a[wized='loginButton'][href='#'][class='login-button w-button']")
    continue_button.click()

@when('I click on "Connect the company"')
def step_impl_when_user_clicks_connect_company(context):
    context.reelly_page.dashboard_page.click_connect_company()

@then('a new tab should open')
def step_impl_then_new_tab_opens(context):
    context.reelly_page.tab_handler.switch_to_new_tab()

@then('I switch to the new tab')
def step_impl_then_user_switches_to_new_tab(context):
    # This step is redundant if 'a new tab should open' already switches tabs
    pass

@then('I should see the title "{expected_title}"')
def step_impl_then_user_sees_title(context, expected_title):
    context.reelly_page.tab_handler.verify_tab(expected_title=expected_title)

@then('the URL should contain "{expected_url}"')
def step_impl_then_user_sees_url(context, expected_url):
    context.reelly_page.tab_handler.verify_tab(expected_url=expected_url)
