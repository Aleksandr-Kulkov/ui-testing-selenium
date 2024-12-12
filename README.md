# ui-testing-selenium


## Description
Проект UI-автотестов на Python.

Тестовая документация: https://docs.google.com/spreadsheets/d/1WskjPgXqzlgsQCBSVYew9OqgGjL0A-3zhIn-jzH4yMA/edit?gid=1640113526#gid=1640113526

Тестовое окружение:
1. OS - Windows 10 Pro 22H2
2. Browser - Chrome 130.0.6723.71 (скачан соответствующий chromedriver).
3. IDE - PyCharm
4. Python - 3.13.0
5. pytest - 8.3.3
6. pytest-selenium - версия 4.1.0
7. selenium - 4.26.1

Тестовые сценарии проверяют функциональность элементов страниц авторизации, регистрации и восстановления пароля.

Перед запуском тестов необходимо:
- скачать архив с файлом chromedriver в соответствии с версией браузера Chrome по ссылке https://developer.chrome.com/docs/chromedriver/downloads?hl=ru, разархивировать архив, переместить папку с файлом chromedriver в папку проекта;
- в файле settings.py в переменной driver_path указать путь до проекта.

Команды для запуска тестов в терминале PyCharm (вместо <path_to_driver> необходимо указать путь до проекта):
1. Страница авторизации: python -m pytest -v --driver Chrome --driver-path <path_to_driver>/ui-testing-selenium/chromedriver-win64/chromedriver.exe tests/test_auth_page.py
2. Страница регистрации: python -m pytest -v --driver Chrome --driver-path <path_to_driver>/ui-testing-selenium/chromedriver-win64/chromedriver.exe tests/test_reg_page.py
3. Страница восстановления пароля: python -m pytest -v --driver Chrome --driver-path <path_to_driver>/ui-testing-selenium/chromedriver-win64/chromedriver.exe tests/test_pass_rec_page.py

При тестировании применен паттерн PageObject.