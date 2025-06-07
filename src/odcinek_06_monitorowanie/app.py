from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from contextlib import contextmanager
import time
import random
import logging
from typing import Generator
from metrics import *

app = Flask(__name__)

# Prometheus metrics
REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP Requests (count)",
    ["method", "endpoint", "params"],
)
BYTES_PROCESSED = Histogram(
    "http_bytes_processed", "Bytes processed in HTTP request/response", ["endpoint"]
)
EXCEPTIONS = Counter("http_exceptions_total", "Total HTTP Exceptions (count)")
SEGMENT_TIME = Histogram(
    "http_segment_time_seconds",
    "Time for code segments in an HTTP request",
    ["endpoint", "segment"],
)

logging.basicConfig(level=logging.INFO)


@app.route("/complex")
@count_requests(REQUESTS)
@track_bytes_processed(BYTES_PROCESSED)
def complex_operation() -> str:
    """Endpoint for a complex operation."""
    response_content = "Complex operation completed."

    with time_segment(SEGMENT_TIME, endpoint="/complex", segment="1-7"):
        time.sleep(0.1 + random.uniform(-0.02, 0.02))

    with time_segment(SEGMENT_TIME, endpoint="/complex", segment="8-14"):
        time.sleep(0.15 + random.uniform(-0.02, 0.02))

    with time_segment(SEGMENT_TIME, endpoint="/complex", segment="15-21"):
        time.sleep(0.05 + random.uniform(-0.02, 0.02))

    return response_content


@app.route("/metrics")
def metrics() -> Response:
    """Endpoint to expose Prometheus metrics."""
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(debug=True)
