import argparse

import arvanapi
import dynamicdns

key = "Apikey 608a6ee4-3aac-4161-b3ad-59bfd7df0865"

domain = "sosori.ir"
record = "dyn"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", type=str)
    parser.add_argument("--domain", type=str)
    parser.add_argument("--record", type=str)
    parser.add_argument("--interval", default=600, type=int)
    args = parser.parse_args()

    a = arvanapi.CDNAPI(key=args.key)
    d = dynamicdns.DynamicDNS(api=a,
                              domain=args.domain,
                              record=args.record,
                              interval=args.interval)
    d.run()
