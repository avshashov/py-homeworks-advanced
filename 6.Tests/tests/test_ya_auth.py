import re
from ya_token import EMAIl
from selenium_auth import open_yandex_auth, get_valid_email

def test_authentication():
    pass

def test_correct_email():
    pattern = r'\w+@((yandex.ru)|(gmail.com)|(mail.ru))'
    correct_email = re.search(pattern, EMAIl).group()

    assert correct_email == EMAIl

