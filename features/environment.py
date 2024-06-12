from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.application import Application


def before_all(context):
    context.browserstack_user = 'alexandralyubche_cX943G'
    context.browserstack_key = 'YhDcZ7qrS1WzpxBpHp4B'


def before_scenario(context, scenario):
    # Initialize the WebDriver with BrowserStack options
    options = Options()
    options.browser_version = 'latest'
    options.platform_name = 'OS X Big Sur'

    bstack_options = {
        'os': 'OS X',
        'osVersion': 'Big Sur',
        'browserName': 'chrome',
        'browserVersion': 'latest',
        'sessionName': scenario.name,
    }
    options.set_capability('bstack:options', bstack_options)

    bs_url = f'http://{context.browserstack_user}:{context.browserstack_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(
        command_executor=bs_url,
        options=options
    )
    context.driver.set_window_size(1024, 768)

    # Initialize the Application object with the WebDriver
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    # Quit the WebDriver after each scenario
    if hasattr(context, 'driver'):
        context.driver.quit()
