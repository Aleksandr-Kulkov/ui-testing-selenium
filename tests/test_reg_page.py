# python -m pytest -v --driver Chrome --driver-path C:/Users/akulkov/PycharmProjects/rostelecom-website/chromedriver-win64/chromedriver.exe tests/test_reg_page.py
import pytest
from settings import *
from pages.auth_page import AuthPage
from pages.reg_page import RegPage


@pytest.fixture(autouse=True)
def reg_page_open(selenium):
    """Фикстура заходит в браузер, открывает страницу авторизации, переходит на страницу регистрации.
    После выполнения теста выходит из браузера."""
    page = AuthPage(selenium)
    # Переход на страницу регистрации.
    page.enter_reg_page()
    yield
    selenium.quit()


def test_reg_empty_fields(selenium):
    """reg_page-001. Валидация отправки пустой формы регистрации."""
    page = RegPage(selenium)
    page.enter_first_name(empty)
    page.enter_last_name(empty)
    page.enter_address(empty)
    page.enter_password(empty)
    page.enter_password_confirm(empty)
    page.btn_click_error_msg()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'
    assert page.msg_last_name.text == msg_reg_last_name, 'msg reg last name error'
    assert page.msg_address.text == msg_address, 'msg address error'
    assert page.msg_password.text == msg_password, 'msg password error'
    assert page.msg_password_confirm.text == msg_password_confirm, 'msg password confirm error'


# Поле "Имя"
def test_reg_empty_first_name(selenium):
    """reg_page_first_name-001. Валидация поля "Имя" с пустым значением."""
    page = RegPage(selenium)
    page.enter_first_name(empty)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password)
    page.btn_click_error_msg_first_name()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'


def test_reg_one_cyrillic_first_name(selenium):
    """reg_page_first_name-002. Валидация поля "Имя" с одним символом (кириллица)."""
    page = RegPage(selenium)
    page.enter_first_name(cyrillic_1)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password)
    page.btn_click_error_msg_first_name()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'


def test_reg_thirty_one_cyrillic_first_name(selenium):
    """reg_page_first_name-007. Валидация поля "Имя" с 31 символом (кириллица и '-')."""
    page = RegPage(selenium)
    page.enter_first_name(cyrillic_31)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password)
    page.btn_click_error_msg_first_name()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'


def test_reg_space_first_name(selenium):
    """reg_page_first_name-008. Валидация поля "Имя" с пробелом."""
    page = RegPage(selenium)
    page.enter_first_name(space)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password)
    page.btn_click_error_msg_first_name()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'


def test_reg_spaces_group_first_name(selenium):
    """reg_page_first_name-009. Валидация поля "Имя" с группой пробелов."""
    page = RegPage(selenium)
    page.enter_first_name(spaces_group)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password)
    page.btn_click_error_msg_first_name()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'


def test_reg_spaces_in_cyrillic_first_name(selenium):
    """reg_page_first_name-010. Валидация поля "Имя" с пробелами в значении (кириллица)."""
    page = RegPage(selenium)
    page.enter_first_name(spaces_in_cyrillic)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password)
    page.btn_click_error_msg_first_name()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'


def test_reg_latin_first_name(selenium):
    """reg_page_first_name-011. Валидация поля "Имя" с латиницей."""
    page = RegPage(selenium)
    page.enter_first_name(latin)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password)
    page.btn_click_error_msg_first_name()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'


def test_reg_digits_first_name(selenium):
    """reg_page_first_name-012. Валидация поля "Имя" с цифрами."""
    page = RegPage(selenium)
    page.enter_first_name(digits)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password)
    page.btn_click_error_msg_first_name()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'


def test_reg_symbols_first_name(selenium):
    """reg_page_first_name-013. Валидация поля "Имя" со спецсимволами."""
    page = RegPage(selenium)
    page.enter_first_name(symbols)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password)
    page.btn_click_error_msg_first_name()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_first_name.text == msg_reg_first_name, 'msg reg first name error'


# Поле "Подтверждение пароля"
def test_reg_invalid_password_confirm(selenium):
    """reg_page_password_confirm-001. Валидация поля "Подтверждение пароля" с password_confirm, отличным от password."""
    page = RegPage(selenium)
    page.enter_first_name(cyrillic_2)
    page.enter_last_name(cyrillic_2)
    page.enter_address(email)
    page.enter_password(password)
    page.enter_password_confirm(password_2)
    page.btn_click_error_msg_password_confirm()

    # Проверка, что регистрация не осуществилась.
    assert page.header.text == 'Регистрация', 'reg error'
    # Проверка сообщений.
    assert page.msg_password_confirm.text == msg_pass_mismatch, 'msg reg password confirm error'
