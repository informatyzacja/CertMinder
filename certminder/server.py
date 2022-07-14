#!/usr/bin/env python3

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


def main() -> None:
    app.run(port=config.app_port)
