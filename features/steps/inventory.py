import time

from behave import *
from selenium import webdriver
from features.steps.pages.inventory_page import InventoryPage


@then('I should be redirected to the "{expected_page}" page')
def step_impl(context, expected_page):
    driver: webdriver = context.browser
    url = driver.current_url
    inventory_page: InventoryPage = InventoryPage(driver)

    mapped_urls: dict = {
        'home': context.page.pageURL,
        'inventory': inventory_page.pageURL
    }

    if expected_page not in mapped_urls.keys():
        raise ValueError('Wrong option sent, please fix')

    assert mapped_urls[expected_page] in url


@then('I should see "{expected_items}" items listed on the page')
def step_impl(context, expected_items):
    driver: webdriver = context.browser
    page: InventoryPage = InventoryPage(driver)

    list_size = len(page.get_all_items())

    assert int(list_size) == int(expected_items)


@then('I should "{expected_to_see}" wrong images on products')
def step_impl(context, expected_to_see):
    driver: webdriver = context.browser
    page: InventoryPage = InventoryPage(driver)

    if expected_to_see == 'see':
        assert page.has_wrong_image(), "Normal images are being displayed"
    elif expected_to_see == 'not see':
        assert not page.has_wrong_image(), "Page is not displaying properly the products image"
    else:
        raise ValueError("Wrong parameter sent")
