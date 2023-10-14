from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@fixture
def selenium_browser_chrome(context: dict):
    context.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield context.browser
    context.browser.quit()


def before_all(context):
    use_fixture(selenium_browser_chrome, context)
