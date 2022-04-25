from elasticsearch import Elasticsearch as es
from config import get_config

config = get_config()

# Create the client instance
client = es(
    config["ELASTIC_SEARCH_URL"],
    ca_certs=config["CA_CERT"],
    basic_auth=("elastic", config["ELASTIC_PASSWORD"])
)


def search_countries_with_name(search_term: str):
    # query = {"match": {"name": search_term}}
    query = {"regexp": { "name": f'.*{search_term}.*'}}
    resp = client.search(index="countries", query=query)

    all_hits = []
    for hit in resp['hits']['hits']:
        all_hits.append(hit["_source"])
    return all_hits


def search_cities_with_name(search_term: str):
    query = {"regexp": { "name": f'.*{search_term}.*'}}
    resp = client.search(index="cities", query=query)

    all_hits = []
    for hit in resp['hits']['hits']:
        all_hits.append(hit["_source"])
    return all_hits

