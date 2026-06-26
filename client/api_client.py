import requests
from requests import Response


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url)
        return response

    def post(self, endpoint: str, data: dict = None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data, **kwargs)
        return response

    def put(self, endpoint: str, data: dict=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=data, **kwargs)
        return response

    def patch(self, endpoint: str, data: dict=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.patch(url, json=data, **kwargs)
        return response

    def delete(self, endpoint: str):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url)
        return response




