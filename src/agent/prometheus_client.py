import requests

PROMETHEUS_URL = "http://localhost:9090"


def query_prometheus(query):
    response = requests.get(
        PROMETHEUS_URL + "/api/v1/query",
        params={
            "query": query
        }
    )

    data = response.json()

    return float(data["data"]["result"][0]["value"][1])


def get_prediction_count():
    return query_prometheus("prediction_total")


def get_model_version():
    return query_prometheus("model_version")


def get_errors_count():
    return query_prometheus("prediction_errors_total")

def get_response_time():
    query = "rate(response_time_seconde_sum[5m])/rate(response_time_seconde_count[5m])"
    return query_prometheus(query)