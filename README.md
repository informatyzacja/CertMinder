# CertMinder

![](https://github.com/informatyzacja-sspwr-projekty/CertMinder/workflows/tests/badge.svg)

Application for reminding about expiring SSL certificates.


## Overview

There are two components of `certminder` – the checker and the server.

The checker periodically scans certificates and stores results in local cache.

The server displays cached results from the local database (sqlite).


## Installation

```
pip install git+https://github.com/informatyzacja-sspwr-projekty/CertMinder.git
```


## Usage

The `certminder` utility is available after the project installation.

```
usage: certminder [-h] [-c] [-s]

Utility to run CertMinder processes (checker, server or both).

options:
  -h, --help     show this help message and exit
  -c, --checker  run the checker process
  -s, --server   run the server process
```

An example configuration file `certminder.yml` is provided in this repository.


## Development

Dedicated tox environment called **run** can be used for development purposes.

E.g. `tox -e run -- certminder` to launch development version without installation.


## Tests

Call `tox` to run the default test suite in this repository.
