from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, headless):
    """
    :param context: Behave context
    :param headless: Run the browser in headless mode if True
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=2560x1440")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.add_argument("--enable-logging")
    options.add_argument("--v=1")
    options.add_argument("--disable-extensions")

    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, headless=True)  # Try non-headless for debugging


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        context.driver.save_screenshot(f"{step.name}_failed.png")
        with open(f"{step.name}_failed.html", "w", encoding="utf-8") as f:
            f.write(context.driver.page_source)
        # Capture console logs
        logs = context.driver.get_log('browser')
        with open(f"{step.name}_console.log", "w") as log_file:
            for entry in logs:
                log_file.write(f"{entry['level']}: {entry['message']}\n")


def after_scenario(context, scenario):
    context.driver.delete_all_cookies()
    context.driver.quit()
