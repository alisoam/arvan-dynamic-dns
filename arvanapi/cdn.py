from .api import API

import aiohttp


class CDNAPI(API):
    def __init__(self, key: str, session: aiohttp.ClientSession = None):
        super().__init__(key=key, path="/cdn/4.0", session=session)

    async def get_domain_information(self, domain: str) -> dict:
        return await self.get(f"/domains/{domain}")

    async def get_list_dns_records(self, domain: str) -> dict:
        return await self.get(f"/domains/{domain}/dns-records")

    async def get_information_dns_record(self, domain: str, id: str) -> dict:
        return await self.get(f"/domains/{domain}/dns-records/{id}")

    async def create_new_dns_record(self, domain: str, body: str) -> dict:
        return await self.post(f"/domains/{domain}/dns-records", body=body)

    async def update_dns_record(self, domain: str, id: str, body: str) -> dict:
        return await self.put(f"/domains/{domain}/dns-records/{id}", body=body)
