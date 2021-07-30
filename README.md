# Arvan Dynamic DNS

A dynamic dns client using Arvan cloud DNS service.
Before start you shoud have a domain in the Arvan cloud pannel.

This script, periodically, updates the selected record in the Arvan cloud DNS
service with the IP address of the running host.

## Usage
for dom1.dyn.example.org
### With Source

``` sh
python3 main.py --key ${API_KEY} --domain example.org --record dom1 --interval 600
```

### With Docker
``` sh
docker run -d --name arvan-dynamic-dns --restart always ghcr.io/alisoam/arvan-dynamic-dns --key $API_KEY --domain sosori.ir --record dom1.dyn
```
