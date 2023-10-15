import time

from behave import *
from selenium import webdriver
from features.steps.pages.inventory_page import InventoryPage


@then('I should be redirected to the "{expected_page}" page')
def step_impl(context, expected_page):
    driver: webdriver = context.browser
    url = driver.current_url
    assert expected_page in url


@then('I should see "{expected_items}" items listed on the page')
def step_impl(context, expected_items):
    driver: webdriver = context.browser
    page: InventoryPage = InventoryPage(driver)

    list_size = len(page.get_all_items())

    assert int(list_size) == int(expected_items)
    time.sleep(3)


@then('I should not see any wrong image on products')
def step_impl(context):
    driver: webdriver = context.browser
    page: InventoryPage = InventoryPage(driver)

    assert not page.has_wrong_image(), "Page is not displaying properly the products image"
