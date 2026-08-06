from monitoring.promotheus_metrics import Counter,Histogram,Gauge

prediction_counter=Counter(
    "prediction_total",
    "total number of prediction"
)

response_time=Histogram(
    "response_time_seconde",
    "response time of prediction API in seconds"
)

error_counter=Counter(
    "prediction_errors_total",
    "total number of prediction errors"
)

model_version=Gauge(
    "model_version",
    "Current deployed model version"
)

