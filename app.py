from flask import Flask, request, jsonify
from flask_cors import CORS

from search_api import search_countries_with_name, search_cities_with_name

app = Flask(__name__)
CORS(app)


@app.route("/")
def base():
    return "<p>Hello, From Search Server!</p>"


@app.route("/search/country")
def search_country():
    partial_search = request.args.get('partialSearch')
    return jsonify(search_countries_with_name(partial_search))


@app.route("/search/city")
def search_cities():
    partial_search = request.args.get('partialSearch')
    return jsonify(search_cities_with_name(partial_search))