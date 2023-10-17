from selenium.webdriver.common.by import By


class BurgerPageLocators:
    MENU_BUTTON_CONTAINER_LOCATOR: str = '#menu_button_container'

    @property
    def burger_menu_button(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.MENU_BUTTON_CONTAINER_LOCATOR} #react-burger-menu-btn')

    @property
    def all_items_link(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.MENU_BUTTON_CONTAINER_LOCATOR} #inventory_sidebar_link')

    @property
    def about_link(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.MENU_BUTTON_CONTAINER_LOCATOR} #about_sidebar_link')

    @property
    def logout_link(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.MENU_BUTTON_CONTAINER_LOCATOR} #logout_sidebar_link')

    @property
    def reset_app_link(self) -> tuple:
        return (By.CSS_SELECTOR, f'{self.MENU_BUTTON_CONTAINER_LOCATOR} #reset_sidebar_link')