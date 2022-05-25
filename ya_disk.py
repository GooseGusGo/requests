import requests
import os


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {"Accept" : "application/json", "Authorization" : f"OAuth {self.token}"}

    def _get_upload_link(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_file: str):
        href = self._get_upload_link(path_to_file=path_to_file).get("href", "")
        response = requests.put(href, data=open((os.path.abspath("test.txt")), 'rb'))
        print("Загружен")


if __name__ == '__main__':
    path_to_file = "test.txt"
    token = ""                        #TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
