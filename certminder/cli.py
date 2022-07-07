#!/usr/bin/env python3

from certminder import checker
from certminder import server


def main() -> None:
    checker.main()
    server.main()
