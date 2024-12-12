from urllib.parse import urlparse

from pytest_selenium import driver


class BasePage(object):
    """Конструктор класса. Принимает на вход объект веб-драйвера,
    адрес страницы и время ожидания элементов"""

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        """Метод возвращает относительный пусть страницы (без домена)."""
        url = urlparse(self.driver.current_url)
        return url.path
