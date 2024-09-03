from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()


# def setup_debug_on_error(userdata, context, scenario):
#     if "DEBUG_ON_ERROR" in userdata and scenario.status == "failed":
#         # -- ENTER DEBUG MODE (ONLY WHEN DEBUG_ON_ERROR is enabled)
#         import pdb; pdb.set_trace()






# from selenium import webdriver


# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from app.application import Application
#
# def browser_init(context, scenario_name):
#     """
#     Initializes the browser instance for the given scenario.
#     :param context: Behave context
#     :param scenario_name: Current scenario name
#     """
#
#     # Uncomment the desired browser setup and comment others to switch the test environment.
#     # Options include Chrome, Firefox, Safari, Headless Chrome, and BrowserStack integration.
#
#     #CHROME Browser setup
#     driver_path = ChromeDriverManager().install()
#     service = Service(driver_path)
#     context.driver = webdriver.Chrome(service=service)
#
#     # FIREFOX Browser setup
#     # driver_path = GeckoDriverManager().install()
#     # service = Service(driver_path)
#     # context.driver = webdriver.Firefox(service=service)
#
#     # SAFARI Browser setup
#     # context.driver = webdriver.Safari()
#
#     # HEADLESS CHROME Browser setup
#     # options = Options()
#     # options.add_argument('--headless')
#     # options.add_argument('--window-size=1920,1080')
#     # service = Service(ChromeDriverManager().install())
#     # context.driver = webdriver.Chrome(options=options, service=service)
#
#     # BROWSERSTACK setup
#     # bs_user = 'your_username'
#     # bs_key = 'your_access_key'
#     # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
#     # options = Options()
#     # bstack_options = {
#     #     'deviceName': 'Google Pixel 5',
#     #     'realMobile': 'true',
#     #     'osVersion': '11.0',
#     #     'sessionName': scenario_name
#     # }
#     # options.set_capability('bstack:options', bstack_options)
#     # context.driver = webdriver.Remote(command_executor=url, options=options)
#
#     # MOBILE EMULATION setup
#     # mobile_emulation = {
#     #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
#     #     "userAgent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36"
#     # }
#     # options = Options()
#     # options.add_experimental_option("mobileEmulation", mobile_emulation)
#     # context.driver = webdriver.Chrome(options=options)
#
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(4)  # Modify implicit wait as necessary
#     context.wait = WebDriverWait(context.driver, 15)  # Modify wait timeout as necessary
#     context.app = Application(context.driver)
#
#
# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     browser_init(context, scenario.name)
#
#
# def before_step(context, step):
#     print('\nStarted step: ', step)
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)
#
#
# def after_scenario(context, scenario):
#     context.driver.quit()
#     print('\nEnded scenario: ', scenario.name)