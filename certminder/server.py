#!/usr/bin/env python3

from flask import Flask
from jinja2 import Environment
from jinja2 import PackageLoader

from certminder import config
from certminder import db


app = Flask(__name__)

j2env = Environment(loader=PackageLoader('certminder', 'templates'))
template = j2env.get_template('index.html.j2')


def get_results() -> dict:
    session = db.session()

    results = session.query(db.Result).all()

    session.close()
    return results


@app.route("/", methods=['GET'])
def index():
    results = get_results()
    return template.render(results=results)


def main() -> None:
    app.run(port=config.app_port)
