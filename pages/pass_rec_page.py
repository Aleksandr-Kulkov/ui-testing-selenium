from pytest_selenium import driver
from pages.base_page import BasePage
from pages.locators import PassRecLocators
from pages.locators import AuthLocators


class PassRecPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)  # обращаемся к методу __init__ родительского класса BasePage,
        # так как новый метод __init__ затрет его.
        # Создание элементов
        self.btn_go_back = driver.find_element(*PassRecLocators.PASS_REC_BTN_GO_BACK)

    def btn_go_back_click(self):
        self.btn_go_back.click()
        self.auth_header = self.driver.find_element(*AuthLocators.AUTH_HEADER)
