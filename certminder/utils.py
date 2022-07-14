#!/usr/bin/env python3

import re


def match_domain(host: str, cnames: list) -> bool:
    if host in cnames:
        return True

    for cname in cnames:
        pattern = cname.replace('.', '[.]').replace('*', '[a-zA-Z0-9_-]+')
        if re.match(pattern, host):
            return True

    return False
