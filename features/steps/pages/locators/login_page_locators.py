from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM_LOCATOR: str = '#login_button_container'
    ERROR_MESSAGE_CONTAINER: str = '.error-message-container'

    @property
    def username_input(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.LOGIN_FORM_LOCATOR} [data-test="username"]')

    @property
    def password_input(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.LOGIN_FORM_LOCATOR} [data-test="password"]')

    @property
    def login_button(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.LOGIN_FORM_LOCATOR} [data-test="login-button"]')

    @property
    def error_message(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.LOGIN_FORM_LOCATOR} [data-test="error"]')
