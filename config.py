ELASTIC_SEARCH_URL = "https://192.168.1.40:9200"
ELASTIC_PASSWORD = "1z6IVKKpByS54r0lh2nD"
CA_CERT = "certs/ca_1650560147848.crt"


def get_config():
    config = {
        "ELASTIC_SEARCH_URL": ELASTIC_SEARCH_URL,
        "ELASTIC_PASSWORD": ELASTIC_PASSWORD,
        "CA_CERT": CA_CERT
    }
    return config
