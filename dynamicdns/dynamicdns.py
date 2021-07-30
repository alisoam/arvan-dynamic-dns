from typing import Union
import ipaddress
import requests
import time

import arvanapi


class DynamicDNS():
    TTL = 120

    def __init__(self, api: arvanapi.CDNAPI, domain: str, record: str, interval: int = 600):
        self.api = api
        self.domain = domain
        self.record = record
        self.interval = interval

        # check the domain
        try:
            _ = api.get_domain_information(domain)
        except requests.HTTPError as e:
            if e.response.status_code == 404:
                raise Exception("domain not found")

    def run(self):
        while True:
            ip = self.ip()
            print(f"\ryour ip address is \"{ip}\" ", end="")

            b = self.body(ip)
            id = self.get_record_id()
            if id is None:
                self.api.create_new_dns_record(domain=self.domain,
                                               body=b)
            else:
                self.api.update_dns_record(domain=self.domain,
                                           id=id,
                                           body=b)
            print("*", end="")

            time.sleep(self.interval)

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

    def get_record_id(self) -> Union[str, None]:
        records = self.api.get_list_dns_records(self.domain)
        for r in records["data"]:
            if r["name"] == self.record:
                return r["id"]
        return None

    @staticmethod
    def ip() -> str:
        r = requests.get("http://ident.me")
        r.raise_for_status()
        return r.text


class Exception(Exception):
    pass
