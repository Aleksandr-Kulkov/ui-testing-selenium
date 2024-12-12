from pytest_selenium import driver
from pages.base_page import BasePage
from pages.locators import RegLocators


class RegPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)  # обращаемся к методу __init__ родительского класса BasePage,
        # так как новый метод __init__ затрет его.
        # Создание элементов
        self.first_name = driver.find_element(*RegLocators.REG_FIRST_NAME)
        self.last_name = driver.find_element(*RegLocators.REG_LAST_NAME)
        self.region = driver.find_element(*RegLocators.REG_REGION)
        self.address = driver.find_element(*RegLocators.REG_ADDRESS)
        self.password = driver.find_element(*RegLocators.REG_PASSWORD)
        self.password_confirm = driver.find_element(*RegLocators.REG_PASSWORD_CONFIRM)
        self.btn = driver.find_element(*RegLocators.REG_BTN)
        self.header = driver.find_element(*RegLocators.REG_HEADER)

    def enter_first_name(self, value):
        self.first_name.send_keys(value)

    def enter_last_name(self, value):
        self.last_name.send_keys(value)

    def enter_region(self, value):
        self.region.send_keys(value)

    def enter_address(self, value):
        self.address.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def enter_password_confirm(self, value):
        self.password_confirm.send_keys(value)

    def btn_click(self):
        self.btn.click()

    # Создание элементов сообщений об ошибках
    def btn_click_error_msg(self):
        self.btn.click()
        self.msg_first_name = self.driver.find_element(*RegLocators.REG_MSG_FIRST_NAME)
        self.msg_last_name = self.driver.find_element(*RegLocators.REG_MSG_LAST_NAME)
        self.msg_address = self.driver.find_element(*RegLocators.REG_MSG_ADDRESS)
        self.msg_password = self.driver.find_element(*RegLocators.REG_MSG_PASSWORD)
        self.msg_password_confirm = self.driver.find_element(*RegLocators.REG_MSG_PASSWORD_CONFIRM)

    def btn_click_error_msg_first_name(self):
        self.btn.click()
        self.msg_first_name = self.driver.find_element(*RegLocators.REG_MSG_FIRST_NAME)

    def btn_click_error_msg_password_confirm(self):
        self.btn.click()
        self.msg_password_confirm = self.driver.find_element(*RegLocators.REG_MSG_PASSWORD_CONFIRM)
