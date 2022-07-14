#!/usr/bin/env python3

import multiprocessing

from certminder import checker
from certminder import server


def main() -> None:
    checker_process = multiprocessing.Process(target=checker.main)
    server_process = multiprocessing.Process(target=server.main)

    checker_process.start()
    server_process.start()

    checker_process.join()
    server_process.join()
