import argparse
import asyncio
import socket

import aiohttp

import arvanapi
import dynamicdns

key = "Apikey 608a6ee4-3aac-4161-b3ad-59bfd7df0865"

domain = "sosori.ir"
record = "dyn"


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", type=str)
    parser.add_argument("--domain", type=str)
    parser.add_argument("--record", type=str)
    parser.add_argument("--interval", default=600, type=int)
    parser.add_argument("-4", dest='four', action="store_true")
    parser.add_argument("-6", dest='six', action="store_true")

    args = parser.parse_args()
    
    f = 0
    if args.four:
        f = socket.AF_INET
    elif args.six:
        f = socket.AF_INET6
    c = aiohttp.TCPConnector(family=f)
    s = aiohttp.ClientSession(connector=c, raise_for_status=True)
    a = arvanapi.CDNAPI(session=s, key=args.key)
    d = dynamicdns.DynamicDNS(api=a,
                              domain=args.domain,
                              record=args.record,
                              interval=args.interval,
                              session=s)
    
    await d.run()


if __name__ == "__main__":
    asyncio.run(main())
