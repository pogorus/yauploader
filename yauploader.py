import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {token}'
        }
        file_name = file_path[file_path.rfind('\\') + 1:]
        response = requests.get(API_BASE_URL + 'v1/disk/resources/upload', params={'path': file_name}, headers=headers)
        upload_url = response.json()['href']
        requests.put(upload_url, headers=headers, files={'file': open(path_to_file, 'rb')})

API_BASE_URL = 'https://cloud-api.yandex.net:443/'

path_to_file = input('Введите путь к файлу: ')
token = input('Введите токен: ')
uploader = YaUploader(token)
result = uploader.upload(path_to_file)