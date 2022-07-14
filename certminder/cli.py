#!/usr/bin/env python3

import multiprocessing
import signal

from certminder import checker
from certminder import server


def handle_sigterm(*args):
    raise KeyboardInterrupt()


def main() -> None:
    checker_process = multiprocessing.Process(target=checker.main)
    server_process = multiprocessing.Process(target=server.main)

    checker_process.start()
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
