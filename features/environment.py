from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from allure_behave.listener import AllureListener
from behave.configuration import Configuration
from behave.runner import Context, Runner
from app.application import Application
import subprocess

def before_all(context: Context):
    context.browserstack_user = 'alexandralyubche_cX943G'
    context.browserstack_key = 'YhDcZ7qrS1WzpxBpHp4B'

    # Allure configuration
    config = Configuration()
    listener = AllureListener(config)
    context.config = config  # Ensure context has the config attribute

def before_scenario(context: Context, scenario):
    options = Options()
    if 'mobile' in scenario.tags:
        # Initialize the WebDriver with BrowserStack options for a Pixel 5 device
        bstack_options = {
            'deviceName': 'Google Pixel 5',
            'realMobile': 'true',
            'osVersion': '11.0',
            'sessionName': scenario.name  # Using the scenario name as the session name
        }
    else:
        # Initialize the WebDriver with BrowserStack options for a desktop environment
        bstack_options = {
            'os': 'OS X',
            'osVersion': 'Big Sur',
            'browserName': 'chrome',
            'browserVersion': 'latest',
            'sessionName': scenario.name  # Using the scenario name as the session name
        }

    options.set_capability('bstack:options', bstack_options)

    bs_url = f'http://{context.browserstack_user}:{context.browserstack_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(
        command_executor=bs_url,
        options=options
    )

    if 'mobile' not in scenario.tags:
        context.driver.set_window_size(1024, 768)

    # Initialize the Application object with the WebDriver
    context.app = Application(context.driver)


def after_scenario(context: Context, scenario):
    # Quit the WebDriver after each scenario
    if hasattr(context, 'driver'):
        context.driver.quit()


def after_all(context: Context):
    allure_results_dir = 'allure-results'
    # Use subprocess to run shell commands instead of os.system
    subprocess.run(['allure', 'generate', allure_results_dir, '-o', 'allure-report', '--clean'])
    subprocess.run(['allure', 'open', 'allure-report'])
