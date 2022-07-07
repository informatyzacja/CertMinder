#!/usr/bin/env python3

from datetime import datetime
from datetime import timedelta
from ssl import SSLError
from urllib import request

from cryptography import x509
import pytz


def get_cert_expiration_from_host(host, port):
    context = request.ssl.create_default_context()

    try:
        with request.socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()

        expire_date = datetime.strptime(cert.get('notAfter'),
                                        '%b %d %H:%M:%S %Y %Z')
        tzone = cert.get('notAfter').split(' ')[-1]
        offset = datetime.now(pytz.timezone(tzone)).utcoffset()
        offset = offset if offset else timedelta(0)

        return expire_date - offset

    except SSLError as e:
        if e.reason == 'CERTIFICATE_VERIFY_FAILED':
            return datetime.utcnow() - timedelta(days=1)
        else:
            raise


def get_cert_expiration_from_file(path):
    with open(path, "rb") as binaryfile:
        pem_data = binaryfile.read()

    cert = x509.load_pem_x509_certificate(pem_data)

    return cert.not_valid_after


def get_days_to_expiration(expire_date):
    expire_in = expire_date - datetime.utcnow()

    return expire_in.days
