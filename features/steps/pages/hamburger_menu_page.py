from .base_page import BasePage
from .locators.hamburger_menu_locators import BurgerPageLocators
from selenium.webdriver.remote import webdriver, webelement


class HamburgerMenuPage(BasePage):
    def __init__(self, driver: webdriver) -> object:
        super().__init__(driver)
        self.locators: BurgerPageLocators = BurgerPageLocators()

    def click_on_hamburger_menu(self) -> None:
        super().click(self.locators.burger_menu_button)

    def click_on_all_items(self) -> None:
        super().click(self.locators.all_items_link)

    def click_on_about(self) -> None:
        super().click(self.locators.about_link)

    def click_on_logout(self) -> None:
        super().click(self.locators.logout_link)

    def click_on_reset(self) -> None:
        super().click(self.locators.reset_app_link)