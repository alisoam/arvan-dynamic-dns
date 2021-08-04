from typing import Union
import ipaddress
import asyncio

import aiohttp

import arvanapi


class DynamicDNS():
    TTL = 120

    def __init__(self, api: arvanapi.CDNAPI, domain: str, record: str,
                 interval: int = 600, session: aiohttp.ClientSession = None):
        self.api = api
        self.domain = domain
        self.record = record
        self.interval = interval

        if session is None:
            print("FUCCKKKK")
            self.session = aiohttp.ClientSession(raise_for_status=True)
        else:
            self.session = session

        # check the domain
        try:
            _ = api.get_domain_information(domain)
        except aiohttp.HTTPError as e:
            if e.response.status_code == 404:
                raise Exception("domain not found")
            raise

    async def run(self):
        while True:
            ip = await self.ip()
            print(f"\ryour ip address is \"{ip}\" ", end="")

            b = self.body(ip)
            id = await self.get_record_id()
            if id is None:
                await self.api.create_new_dns_record(domain=self.domain,
                                               body=b)
            else:
                await self.api.update_dns_record(domain=self.domain,
                                           id=id,
                                           body=b)
            print("*", end="")

        await asyncio.sleep(self.interval)

    def body(self, addr: str) -> dict:
        ip = ipaddress.ip_address(addr)
        if ip.version == 4:
            t = "a"
        elif ip.version == 6:
            t = "aaaa"
        else:
            raise Exception("wrong ip address")

        b = {"type": t,
             "name": self.record,
             "value": [{"ip": addr}],
             "ttl": self.TTL}
        return b

    async def get_record_id(self) -> Union[str, None]:
        records = await self.api.get_list_dns_records(self.domain)
        for r in records["data"]:
            if r["name"] == self.record:
                return r["id"]
        return None

    async def ip(self) -> str:
        async with self.session.get("http://ident.me") as r:
            return await r.text()


class Exception(Exception):
    pass
