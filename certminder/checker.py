#!/usr/bin/env python3

from datetime import datetime

from certminder.certificate import Cert
from certminder import config
from certminder import db
from certminder.utils import match_domain


def update() -> None:
    session = db.session()

    for entry in config.to_verify:
        host = entry.get('host')
        port = entry.get('port', 443)

        cert = Cert(host, port)
        now = datetime.utcnow()

        start = (cert.get_start_date() < now)
        end = (cert.get_end_date() > now)
        name = match_domain(host, cert.get_common_name())
        valid = True  # TODO

        db.Result.create_or_update(
            session, host, port,
            start, end, name, valid
        )

    session.close()


def main() -> None:
    update()
