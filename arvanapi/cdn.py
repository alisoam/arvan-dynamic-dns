from .api import API


class CDNAPI(API):
    def __init__(self, key: str):
        super().__init__(key, "/cdn/4.0")

    def get_domain_information(self, domain: str) -> dict:
        return self.get(f"/domains/{domain}")

    def get_list_dns_records(self, domain: str) -> dict:
        return self.get(f"/domains/{domain}/dns-records")

    def get_information_dns_record(self, domain: str, id: str) -> dict:
        return self.get(f"/domains/{domain}/dns-records/{id}")

    def create_new_dns_record(self, domain: str, body: str) -> dict:
        return self.post(f"/domains/{domain}/dns-records", body=body)

    def update_dns_record(self, domain: str, id: str, body: str) -> dict:
        return self.put(f"/domains/{domain}/dns-records/{id}", body=body)
