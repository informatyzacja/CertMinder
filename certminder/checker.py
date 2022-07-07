#!/usr/bin/env python3

from certminder import config
from certminder.expiration import get_cert_expiration_from_host
from certminder.expiration import get_days_to_expiration


def check(host, port=443):
    date = get_cert_expiration_from_host(host, port)
    identifier = f'{host}:{port}'

    days = get_days_to_expiration(date)

    return identifier, days


def main() -> None:
    for entry in config.to_verify:
        host = entry.get('host')
        port = entry.get('port', 443)
        print(check(host, port))
