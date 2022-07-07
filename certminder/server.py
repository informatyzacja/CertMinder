#!/usr/bin/env python3

import signal

from flask import Flask
from jinja2 import Environment
from jinja2 import PackageLoader

from certminder import config


app = Flask(__name__)

j2env = Environment(loader=PackageLoader('certminder', 'templates'))
template = j2env.get_template('index.html.j2')


@app.route("/", methods=['GET'])
def index():
    return template.render()


def handle_sigterm(*args):
    raise KeyboardInterrupt()


def main() -> None:
    signal.signal(signal.SIGTERM, handle_sigterm)
    app.run(port=config.app_port)
