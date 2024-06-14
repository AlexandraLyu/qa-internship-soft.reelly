from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param scenario_name:
    :param context: Behave context
    """

    # ## CHROME Browser #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ##  FIREFOX Browser #
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ## SAFARI Browser #
    # context.driver = webdriver.Safari()

    # HEADLESS MODE
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window--size=1920*1080')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )
    # driver.set_window_size(1920, 1080)

    # BROWSERSTACK #|

    # bs_user = 'alexandralyubche_cX943G'
    # bs_key = 'YhDcZ7qrS1WzpxBpHp4B'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options = {
    #     'deviceName': 'Google Pixel 5',
    #     'realMobile': 'true',
    #     'osVersion': '11.0',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 540, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True}}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)
    context.app = Application(context.driver)
    # context.driver.maximize_window()


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    # logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        # Screenshot:
        # context.driver.save_screenshot(f'step_failed_{step}.png')
        print('\nStep failed: ', step)
        # logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()