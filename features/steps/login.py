import time

from behave import *
from selenium import webdriver
from features.steps.pages.login_page import LoginPage


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
    # time.sleep(5)
