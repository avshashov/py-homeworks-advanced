from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from ya_token import PASSWORD, EMAIl


def get_valid_email(email):
    return email


def open_yandex_auth(email):
    # options = ChromeOptions()
    # options.add_experimental_option('detach', True)
    # yandex_page = webdriver.Chrome(options=options)
    yandex_page = webdriver.Chrome()
    yandex_page.implicitly_wait(30)

    yandex_page.get('https://passport.yandex.ru/auth/')

    login = yandex_page.find_element(By.NAME, 'login')
    login.send_keys(email)
    sign_in_button = yandex_page.find_element(By.ID, 'passp:sign-in')
    sign_in_button.click()

    password = yandex_page.find_element(By.NAME, 'passwd')
    password.send_keys(PASSWORD)
    sign_in_button = yandex_page.find_element(By.ID, 'passp:sign-in')
    sign_in_button.click()

# email = get_valid_email(EMAIl)
# open_yandex_auth(email)

