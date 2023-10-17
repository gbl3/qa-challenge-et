import time

from behave import *
from selenium import webdriver
from features.steps.pages.login_page import LoginPage
from features.steps.pages.inventory_page import InventoryPage
from features.steps.pages.hamburger_menu_page import HamburgerMenuPage


@given('I am on SauceDemo homepage')
def step_impl(context):
    page: LoginPage = context.page
    driver: webdriver = context.browser
    page.visit()
    url = driver.current_url
    assert page.pageURL in url


@given('I am logged out')
def step_impl(context):
    page: LoginPage = context.page

    assert page.is_username_input_visible()
    assert page.is_password_input_visible()


@given('I am logged in')
def step_impl(context):
    login_page: LoginPage = context.page
    inventory_page = InventoryPage(context.browser)

    login_page.visit()
    login_page.fill_username('standard_user')
    login_page.fill_password('secret_sauce')
    login_page.click_on_login_button()

    url = context.browser.current_url
    assert inventory_page.pageURL in url


@when('I type my username "{username}"')
def step_impl(context, username):
    page: LoginPage = context.page
    page.fill_username(username)


@when('I type my password "{password}"')
def step_impl(context, password):
    page: LoginPage = context.page
    page.fill_password(password)


@when('I click on the Login button')
def step_impl(context):
    page: LoginPage = context.page
    page.click_on_login_button()


@when('I click on the hamburger menu button')
def step_impl(context):
    page: HamburgerMenuPage = HamburgerMenuPage(context.browser)
    page.click_on_hamburger_menu()


@when('I click on the "{link_to_click}" link inside the hamburger menu')
def step_impl(context, link_to_click):
    page: HamburgerMenuPage = HamburgerMenuPage(context.browser)
    mapped_links: dict = {
        'all items': page.click_on_all_items,
        'about': page.click_on_about,
        'logout': page.click_on_hamburger_menu,
        'reset app': page.click_on_reset
    }

    if link_to_click not in mapped_links.keys():
        raise ValueError('Wrong option sent, please fix')

    mapped_links[link_to_click]()


@then('I should see the error message "{error_message}"')
def step_impl(context, error_message):
    page: LoginPage = context.page
    assert error_message in page.get_error_message()