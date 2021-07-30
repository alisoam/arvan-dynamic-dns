import json
import requests


class API():
    API_GATEWAY_PATH = "https://napi.arvancloud.com"

    def __init__(self, key: str, path: str):
        self.key = key
        self.path = path

    def request(self, path, params, body=None) -> dict:
        u = self.url(path)
        h = {"Authorization": self.key,
             "Content-Type": "application/json",
             "Accept": "application/json"}
        return {"headers": h,
                "url": u,
                "params": params,
                "data": json.dumps(body)}

    def get(self, path: str, params: dict = None) -> dict:
        kw = self.request(path, params)
        r = requests.get(**kw)
        r.raise_for_status()
        return r.json()

    def post(self, path: str, body: dict = None, params: dict = None) -> dict:
        kw = self.request(path, params, body)
        r = requests.post(**kw)
        r.raise_for_status()
        return r.json()

    def put(self, path: str, body: dict = None, params: dict = None) -> dict:
        kw = self.request(path, params, body)
        r = requests.put(**kw)
        r.raise_for_status()
        return r.json()

    def url(self, path: str) -> str:
        return self.base_url + path

    @property
    def base_url(self) -> str:
        return self.API_GATEWAY_PATH + self.path
