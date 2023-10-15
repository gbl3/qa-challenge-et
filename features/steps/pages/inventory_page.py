from .base_page import BasePage
from .locators.inventory_page_locators import InventoryPageLocators
from selenium.webdriver.remote import webdriver, webelement
from selenium.common.exceptions import TimeoutException


class InventoryPage(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.locators: InventoryPageLocators = InventoryPageLocators()
        self.pageURL: str = 'https://www.saucedemo.com/inventory'

    def visit(self) -> None:
        self.driver.get(self.pageURL)

    def get_all_items(self) -> list[webelement]:
        return super().get_elements(self.locators.inventory_items)

    def has_wrong_image(self) -> bool:
        try:
            super().wait_for_element(self.locators.wrong_image(), 3)
            return True
        except TimeoutException:
            return False
