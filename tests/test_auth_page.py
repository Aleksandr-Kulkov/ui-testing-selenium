# python -m pytest -v --driver Chrome --driver-path C:/Users/akulkov/PycharmProjects/rostelecom-website/chromedriver-win64/chromedriver.exe tests/test_auth_page.py
import pytest
from pages.auth_page import AuthPage
from settings import empty, email, phone, login, ls


def test_auth_empty_fields(selenium):
    """auth_page_phone-001. Валидация отправки пустой формы авторизации."""
    page = AuthPage(selenium)
    page.enter_username(empty)
    page.enter_password(empty)
    page.btn_click()

    # Проверка, что авторизация не осуществилась.
    assert page.header.text == 'Авторизация', 'auth error'


def test_change_tab_from_phone_to_email(selenium):
    """auth_page_phone-002. Валидация переключения таба с phone на email при вводе в поле телефона значения эл. почты."""
    page = AuthPage(selenium)
    page.tab_phone_click()
    page.enter_username(email)
    page.header_click()

    # Проверка, что таб выбора аутентификации меняется автоматически с phone на email.
    assert page.tab.get_attribute('value') == 'EMAIL', 'tab phone error'


def test_change_tab_from_email_to_phone(selenium):
    """auth_page_email-001. Валидация переключения таба с email на phone при вводе в поле эл. почты значения телефона."""
    page = AuthPage(selenium)
    page.tab_email_click()
    page.enter_username(phone)
    page.header_click()

    # Проверка, что таб выбора аутентификации меняется автоматически с email на phone.
    assert page.tab.get_attribute('value') == 'PHONE', 'tab email error'


def test_change_tab_from_email_to_login(selenium):
    """auth_page_email-002. Валидация переключения таба с email на login при вводе в поле эл. почты значения логина."""
    page = AuthPage(selenium)
    page.tab_email_click()
    page.enter_username(login)
    page.header_click()

    # Проверка, что таб выбора аутентификации меняется автоматически с email на login.
    assert page.tab.get_attribute('value') == 'LOGIN', 'tab email error'


def test_change_tab_from_email_to_ls(selenium):
    """auth_page_email-003. Валидация переключения таба с email на ls при вводе в поле эл. почты значения лицевого счета."""
    page = AuthPage(selenium)
    page.tab_email_click()
    page.enter_username(ls)
    page.header_click()

    # Проверка, что таб выбора аутентификации меняется автоматически с email на login.
    assert page.tab.get_attribute('value') == 'LS', 'tab email error'


def test_change_tab_from_login_to_phone(selenium):
    """auth_page_login-001. Валидация переключения таба с login на phone при вводе в поле логина значения телефона."""
    page = AuthPage(selenium)
    page.tab_login_click()
    page.enter_username(phone)
    page.header_click()

    # Проверка, что таб выбора аутентификации меняется автоматически с login на phone.
    assert page.tab.get_attribute('value') == 'PHONE', 'tab login error'


def test_change_tab_from_login_to_email(selenium):
    """auth_page_login-002. Валидация переключения таба с login на email при вводе в поле логина значения эл. почты."""
    page = AuthPage(selenium)
    page.tab_login_click()
    page.enter_username(email)
    page.header_click()

    # Проверка, что таб выбора аутентификации меняется автоматически с login на email.
    assert page.tab.get_attribute('value') == 'EMAIL', 'tab login error'


@pytest.mark.xfail(reason='BR-001')
def test_change_tab_from_login_to_ls(selenium):
    """auth_page_login-003. Валидация переключения таба с login на ls при вводе в поле логина значения лицевого счета."""
    page = AuthPage(selenium)
    page.tab_login_click()
    page.enter_username(ls)
    page.header_click()

    # Проверка, что таб выбора аутентификации меняется автоматически с login на ls.
    assert page.tab.get_attribute('value') == 'LS', 'tab login error'
