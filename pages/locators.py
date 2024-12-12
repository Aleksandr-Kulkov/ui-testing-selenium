from selenium.webdriver.common.by import By


class AuthLocators:
    # auth_page
    AUTH_USERNAME = (By.ID, 'username')
    AUTH_PASSWORD = (By.ID, 'password')
    AUTH_BTN = (By.ID, 'kc-login')
    AUTH_HEADER = (By.ID, 'card-title')
    AUTH_TAB = (By.XPATH, '//input[@name="tab_type"]')
    AUTH_TAB_PHONE = (By.ID, 't-btn-tab-phone')
    AUTH_TAB_EMAIL = (By.ID, 't-btn-tab-mail')
    AUTH_TAB_LOGIN = (By.ID, 't-btn-tab-login')
    AUTH_LINK_TO_REG_PAGE = (By.ID, 'kc-register')
    AUTH_LINK_TO_PASS_REC_PAGE = (By.ID, 'forgot_password')


class RegLocators:
    # reg_page
    REG_FIRST_NAME = (By.NAME, 'firstName')
    REG_LAST_NAME = (By.NAME, 'lastName')
    REG_REGION = (By.XPATH, '//input[@class="rt-input__input rt-select__input rt-input__input--rounded' \
                            ' rt-input__input--orange"]')
    REG_ADDRESS = (By.ID, 'address')
    REG_PASSWORD = (By.ID, 'password')
    REG_PASSWORD_CONFIRM = (By.ID, 'password-confirm')
    REG_BTN = (By.NAME, 'register')
    REG_HEADER = (By.ID, 'card-title')
    REG_MSG_FIRST_NAME = (By.XPATH, '//*[@class="name-container"]/div[1]/span')
    REG_MSG_LAST_NAME = (By.XPATH, '//*[@class="name-container"]/div[2]/span')
    REG_MSG_ADDRESS = (By.XPATH, '//*[@class="register-form__address"]/div/span')
    REG_MSG_PASSWORD = (By.XPATH, '//*[@class="new-password-container"]/div[1]/span')
    REG_MSG_PASSWORD_CONFIRM = (By.XPATH, '//*[@class="new-password-container"]/div[2]/span')


class PassRecLocators:
    # pass_rec_page
    PASS_REC_BTN_GO_BACK = (By.ID, 'reset-back')
