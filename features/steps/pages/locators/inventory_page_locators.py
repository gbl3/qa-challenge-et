from selenium.webdriver.common.by import By


class InventoryPageLocators:
    INVENTORY_CONTAINER_LOCATOR: str = '#inventory_container'

    @property
    def inventory_items(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.INVENTORY_CONTAINER_LOCATOR} .inventory_item')

    @property
    def wrong_image(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.INVENTORY_CONTAINER_LOCATOR} img[src*="404"]')