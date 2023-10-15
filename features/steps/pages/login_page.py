from .base_page import BasePage
from .locators.login_page_locators import LoginPageLocators
from selenium.webdriver.remote import webdriver, webelement


class LoginPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.locators: LoginPageLocators = LoginPageLocators()
        self.pageURL: str = 'https://www.saucedemo.com/'

    def visit(self) -> None:
        self.driver.get(self.pageURL)

    def get_username_input(self) -> webelement:
        return super().get_element(self.locators.username_input)

    def is_username_input_visible(self) -> bool:
        return super().is_visible(self.locators.username_input)

    def is_password_input_visible(self) -> bool:
        return super().is_visible(self.locators.username_input)

    def get_password_input(self) -> webelement:
        return super().get_element(self.locators.password_input)

    def fill_username(self, username: str) -> None:
        super().fill_in(self.locators.username_input, username)

    def fill_password(self, password: str) -> None:
        super().fill_in(self.locators.password_input, password)

    def click_on_login_button(self) -> None:
        super().click(self.locators.login_button)





