import requests

class YandexConnect:

    def __init__(self, token):
        self.token = token

    def create_folder(self, folder_name):
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        params = {
            'path': f'{folder_name}'
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=headers)
        self.status_code = response.status_code

    def value_status_code(self):
        return self.status_code
    
    def delete_folder(self, folder_name):
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        params = {
            'path': f'{folder_name}',
            'permanently': True
        }
        requests.delete('https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=headers)