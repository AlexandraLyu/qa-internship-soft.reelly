from behave import given, when, then
from selenium import webdriver
from selenium.common.exceptions import (
    TimeoutException, ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.SettingsPage import SettingsPage
from pages.change_password_page import ChangePasswordPage


def wait_for_element(context, by, value, timeout=20):
    """Helper function to wait for an element to be present and visible."""
    try:
        wait = WebDriverWait(context.driver, timeout)
        element = wait.until(EC.visibility_of_element_located((by, value)))
        return element
    except (TimeoutException, ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException) as e:
        print(f"Error waiting for element by {by} with value {value}: {e}")
        print(context.driver.page_source)  # Output HTML source for debugging
        context.driver.quit()
        raise e


@given('I am logged in on the main page')
def step_impl_logged_in_on_main_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://soft.reelly.io")

    try:
        email_field = wait_for_element(context, By.CSS_SELECTOR, "input#email-2")
        email_field.clear()
        email_field.send_keys("lybchevskaya@icloud.com")

        password_field = wait_for_element(context, By.CSS_SELECTOR, "input#field")
        password_field.clear()
        password_field.send_keys("Abundance88!")

        continue_button = wait_for_element(context, By.CSS_SELECTOR, "a[wized='loginButton'][href='#'][class='login-button w-button']")
        continue_button.click()

    except Exception as e:
        print(f"Error during login: {e}")
        context.driver.quit()
        raise e

    context.add_cleanup(context.driver.quit)


@when('I navigate to the settings page')
def step_impl_navigate_to_settings(context):
    try:
        menu_block = wait_for_element(context, By.CSS_SELECTOR, ".menu-block")
        context.driver.execute_script("arguments[0].scrollIntoView(true);", menu_block)

        settings_button = wait_for_element(context, By.XPATH, "//div[contains(@class, 'menu-button-text') and normalize-space(text())='Settings']")
        settings_button.click()

    except Exception as e:
        print(f"Error navigating to settings menu: {e}")
        context.driver.quit()
        raise e


@when('I select the Change password option')
def step_impl_select_change_password(context):
    try:
        change_password_button = wait_for_element(context, By.CSS_SELECTOR, "a[href='/set-new-password'].page-setting-block.w-inline-block")
        change_password_button.click()
    except Exception as e:
        print(f"Error clicking Change password button: {e}")
        context.driver.quit()
        raise e


@then('I should be on the Change Password page')
def step_impl_verify_on_change_password_page(context):
    context.change_password_page = ChangePasswordPage(context.driver)
    try:
        assert context.change_password_page.verify_change_password_page(), "Not on Change Password page"
    except AssertionError as e:
        print(f"Verification failed: {e}")
        context.driver.quit()
        raise e


@when('I enter "{new_password}" as the new password')
def step_impl_enter_new_password(context, new_password):
    try:
        new_password_input = wait_for_element(context, By.CSS_SELECTOR, "#Enter-new-password")
        new_password_input.clear()
        new_password_input.send_keys(new_password)
    except Exception as e:
        print(f"Error entering new password: {e}")
        context.driver.quit()
        raise e


@when('I enter "{repeat_password}" as the repeated password')
def step_impl_enter_repeat_password(context, repeat_password):
    try:
        repeat_password_input = wait_for_element(context, By.CSS_SELECTOR, "#Repeat-password")
        repeat_password_input.clear()
        repeat_password_input.send_keys(repeat_password)
    except Exception as e:
        print(f"Error entering repeated password: {e}")
        context.driver.quit()
        raise e


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('the "Change password" button should be enabled')
def step_impl_verify_button_enabled(context):
    wait = WebDriverWait(context.driver, 10)  # Set up WebDriver wait

    try:
        # Locate the "Change password" button using the updated locator
        change_password_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@wized='changePasswordButton']"))
        )

        # Check if the button is enabled
        assert change_password_button.is_enabled(), "Change password button is not enabled"
    except Exception as e:
        print(f"Button verification failed: {e}")
        context.driver.quit()
        raise e





