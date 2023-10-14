from behave import *
from selenium import webdriver


@given('I am on SauceDemo homepage')
def step_impl(context):
    driver: webdriver = context.browser
    driver.get('https://www.saucedemo.com/')
