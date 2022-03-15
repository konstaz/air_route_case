import flask
import os

from flask import Flask, request, jsonify


app = Flask(__name__)

examples = [
    "01-create-route",
    "02-get-route",
    "03-update-route",
    "04-delete-route",
    "05-retrieve-routes",
]


@app.route("/")
def show_list():
    body = ""
    for example in examples:
        body += f'<a href="/{example}">{example}</a><br>'
    return body


@app.route("/<example>", methods=["GET", "POST"])
def run_example(example=None):
    print(f'TYYPYYPYPPYPYPYP ::::: {request.args}')
    data = request.args if not request.get_json() else request.get_json()
    print(f'TYYPYYPYPPYPYPYP ::::: {data}')
    if example not in examples:
        flask.abort(404, "Example does not exist")
    return __import__(example).main(data)


if __name__ == "__main__":
    app.debug = True
    app.run()
