#!/usr/bin/env python3

import argparse
import multiprocessing
import signal

from certminder import checker
from certminder import server


def handle_sigterm(*args):
    raise KeyboardInterrupt()


def main() -> None:
    parser = argparse.ArgumentParser(description='''
        Utility to run CertMinder processes (checker, server or both).
    ''')
    parser.add_argument('-c', '--checker', dest='checker',
                        default=False, action='store_true',
                        help='run the checker process')
    parser.add_argument('-s', '--server', dest='server',
                        default=False, action='store_true',
                        help='run the server process')

    args = parser.parse_args()

    if not args.checker and not args.server:
        parser.print_help()

    checker_process = multiprocessing.Process(target=checker.main)
    server_process = multiprocessing.Process(target=server.main)

    if args.checker:
        checker_process.start()
    if args.server:
        server_process.start()

    signal.signal(signal.SIGTERM, handle_sigterm)

    try:
        if checker_process.is_alive():
            checker_process.join()
        if server_process.is_alive():
            server_process.join()
    except KeyboardInterrupt:
        if checker_process.is_alive():
            checker_process.terminate()
        if server_process.is_alive():
            server_process.terminate()
    else:
        checker_process.close()
        server_process.close()
