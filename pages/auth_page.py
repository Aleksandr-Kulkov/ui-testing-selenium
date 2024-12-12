from pytest_selenium import driver
from pages.base_page import BasePage
from pages.locators import AuthLocators
from settings import auth_page_url


class AuthPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)  # обращаемся к методу __init__ родительского класса BasePage,
        # так как новый метод __init__ затрет его.
        url = auth_page_url
        driver.get(url)
        # Создание нужных элементов
        self.username = driver.find_element(*AuthLocators.AUTH_USERNAME)
        self.password = driver.find_element(*AuthLocators.AUTH_PASSWORD)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.header = driver.find_element(*AuthLocators.AUTH_HEADER)
        self.tab = driver.find_element(*AuthLocators.AUTH_TAB)
        self.tab_phone = driver.find_element(*AuthLocators.AUTH_TAB_PHONE)
        self.tab_email = driver.find_element(*AuthLocators.AUTH_TAB_EMAIL)
        self.tab_login = driver.find_element(*AuthLocators.AUTH_TAB_LOGIN)
        self.link_to_reg_page = driver.find_element(*AuthLocators.AUTH_LINK_TO_REG_PAGE)
        self.link_to_pass_rec_page = driver.find_element(*AuthLocators.AUTH_LINK_TO_PASS_REC_PAGE)

    def enter_username(self, value):
        self.username.send_keys(value)

    def enter_password(self, value):
        self.password.send_keys(value)

    def btn_click(self):
        self.btn.click()

    def header_click(self):
        self.header.click()

    def tab_phone_click(self):
        self.tab_phone.click()

    def tab_email_click(self):
        self.tab_email.click()

    def tab_login_click(self):
        self.tab_login.click()

    def enter_reg_page(self):
        self.link_to_reg_page.click()

    def enter_pass_rec_page(self):
        self.link_to_pass_rec_page.click()
