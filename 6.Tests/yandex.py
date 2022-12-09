import ya_token
import requests


def create_folder(foldername='Тестовая папка'):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Authorization': f'OAuth {ya_token.token}'}
    params = {'path': foldername}

    response = requests.put(url=url, headers=headers, params=params)
    return response.status_code

