import json

import aiohttp


class API():
    API_GATEWAY_PATH = "https://napi.arvancloud.com"

    def __init__(self, key: str, path: str, session: aiohttp.ClientSession = None):
        self.key = key
        self.path = path
        if session:
            self.session = session
        else:
            self.session = aiohttp.ClientSession(raise_for_status=True)

    def request(self, path, params, body=None) -> dict:
        u = self.url(path)
        h = {"Authorization": self.key,
             "Content-Type": "application/json",
             "Accept": "application/json"}
        return {"headers": h,
                "url": u,
                "params": params,
                "data": json.dumps(body)}

    async def get(self, path: str, params: dict = None) -> dict:
        kw = self.request(path, params)
        async with self.session.get(**kw) as r:
            return await r.json()

    async def post(self, path: str, body: dict = None, params: dict = None) -> dict:
        kw = self.request(path, params, body)
        async with self.session.post(**kw) as r:
            return await r.json()

    async def put(self, path: str, body: dict = None, params: dict = None) -> dict:
        kw = self.request(path, params, body)
        async with self.session.put(**kw) as r:
            return await r.json()

    def url(self, path: str) -> str:
        return self.base_url + path

    @property
    def base_url(self) -> str:
        return self.API_GATEWAY_PATH + self.path
