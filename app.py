from flask import Flask, request, jsonify
from flask_cors import CORS

from search_api import search_with_name

app = Flask(__name__)
CORS(app)


@app.route("/")
def base():
    return "<p>Hello, From Search Server!</p>"


@app.route("/search")
def search():
    partial_search = request.args.get('partialSearch')
    return jsonify(search_with_name(partial_search))