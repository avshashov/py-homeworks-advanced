from yandex import create_folder
import ya_token
import requests

def test_create_folder():
    status_code = create_folder()
    assert status_code == 201

def test_exists_folder():
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {ya_token.token}'}
    params = {'path': 'Тестовая папка'}
    response = requests.get(url=url, headers=headers, params=params)

    assert response.json()['name'] == 'Тестовая папка'

def test_folder_already_exists():
    status_code = create_folder()
    assert status_code == 409
