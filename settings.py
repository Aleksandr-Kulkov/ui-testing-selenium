# URL
auth_page_url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth' \
                '?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/' \
                'login&response_type=code&scope=openid&state=6c6800ba-2e66-450a-a019-17c3879780bd&theme&auth_type'

# Path
driver_path = 'C:/Users/akulkov/PycharmProjects/ui-testing-selenium/chromedriver-win64/chromedriver.exe'

# Test Data
empty = ''
email = 'test@mail.com'
phone = '+79876543210'
login = '12345678'
ls = '123456789101'
cyrillic_2 = 'йЮ'
cyrillic_1 = 'ц'
cyrillic_31 = 'ОаВЧмКЙлЦТГр-еумцгзтючсЙьлвдлзп'
latin = 'nmLBpSDENzwHFNbTHMwfLoviWXgmZ'
password = 'Test1234'
password_2 = 'Test12345'
space = ' '
spaces_group = '    '
spaces_in_cyrillic = ' ЗЁтЮы ЯеБЗЭ  ОЪйХФ   ршЛмцрФХР  '
digits = '123'
symbols = '~!@#$%^&*()_+{}[]/|\<>,."№;:?='

# Messages
msg_reg_first_name = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
msg_reg_last_name = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
msg_address = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
msg_password = 'Длина пароля должна быть не менее 8 символов'
msg_password_confirm = 'Длина пароля должна быть не менее 8 символов'
msg_pass_mismatch = 'Пароли не совпадают'
