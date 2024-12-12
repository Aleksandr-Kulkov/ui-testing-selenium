# python -m pytest -v --driver Chrome --driver-path C:/Users/akulkov/PycharmProjects/rostelecom-website/chromedriver-win64/chromedriver.exe tests/test_pass_rec_page.py
import pytest
from pages.auth_page import AuthPage
from pages.pass_rec_page import PassRecPage


@pytest.fixture(autouse=True)
def pass_rec_page_open(selenium):
    """Фикстура заходит в браузер, открывает страницу авторизации, переходит на страницу восстановления пароля.
    После выполнения теста выходит из браузера."""
    page = AuthPage(selenium)
    # Переход на страницу восстановления пароля.
    page.enter_pass_rec_page()
    yield
    selenium.quit()


def test_pass_rec_btn_go_back(selenium):
    """pass_rec_page-001. Валидация кнопки возврата на страницу авторизации."""
    page = PassRecPage(selenium)
    page.btn_go_back_click()

    # Проверка, что возврат на страницу авторизации осуществился.
    assert page.auth_header.text == 'Авторизация', 'pass rec page error'
