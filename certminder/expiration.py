#!/usr/bin/env python3

from datetime import datetime
from ssl import CERT_NONE
from ssl import DER_cert_to_PEM_cert
from urllib import request

from cryptography import x509


def get_cert_expiration_from_host(host, port):
    context = request.ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = CERT_NONE

    with request.socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            der_data = ssock.getpeercert(True)

    pem_data = DER_cert_to_PEM_cert(der_data)
    cert = x509.load_pem_x509_certificate(str.encode(pem_data))

    return cert.not_valid_after


def get_cert_expiration_from_file(path):
    with open(path, "rb") as binaryfile:
        pem_data = binaryfile.read()

    cert = x509.load_pem_x509_certificate(pem_data)

    return cert.not_valid_after


def get_days_to_expiration(expire_date):
    expire_in = expire_date - datetime.utcnow()

    return expire_in.days
