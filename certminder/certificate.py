#!/usr/bin/env python3

from ssl import CERT_NONE
from ssl import DER_cert_to_PEM_cert
from urllib import request

from cryptography import x509


class Cert(object):
    def __init__(self, host: str, port: int) -> x509.Certificate:
        context = request.ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = CERT_NONE

        with request.socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                der_data = ssock.getpeercert(True)

        pem_data = DER_cert_to_PEM_cert(der_data)
        self.cert = x509.load_pem_x509_certificate(str.encode(pem_data))

    def get_start_date(self) -> int:
        return self.cert.not_valid_before

    def get_end_date(self) -> int:
        return self.cert.not_valid_after

    def get_common_name(self) -> list:
        ext = self.cert.extensions.get_extension_for_oid(
            x509.oid.ExtensionOID.SUBJECT_ALTERNATIVE_NAME
        )
        return ext.value.get_values_for_type(x509.DNSName)

        # Alternative:
        # TODO: Check what's the difference and if it is worth to support it
        # return [cname.value
        #         for cname in self.cert.subject.get_attributes_for_oid(
        #             x509.oid.NameOID.COMMON_NAME
        #         )]
