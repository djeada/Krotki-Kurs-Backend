from functools import wraps
from flask import request
from prometheus_client import Counter, Histogram
from contextlib import contextmanager
import time
import sys

# Prometheus metric recording context manager
@contextmanager
def time_segment(metric, endpoint: str, segment: str):
    """Context manager for timing a code segment."""
    start = time.time()
    try:
        yield
    finally:
        duration = time.time() - start
        metric.labels(endpoint=endpoint, segment=segment).observe(duration)


def format_params(params) -> str:
    """Format the query parameters for metrics."""
    return ",".join([f"{k}:{''.join(v)}" for k, v in sorted(params.items())])


def calculate_size(obj) -> int:
    """Calculate the size of a Python object in bytes."""
    return sys.getsizeof(obj)


# Decorator for request counting
def count_requests(counter: Counter):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            params = format_params(request.args)
            counter.labels(
                method=request.method, endpoint=request.path, params=params
            ).inc()
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Decorator for tracking bytes processed
def track_bytes_processed(histogram: Histogram):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            request_size = calculate_size(request.data)
            response_size = calculate_size(response)
            total_bytes = request_size + response_size
            histogram.labels(endpoint=request.path).observe(total_bytes)
            return response

        return wrapper

    return decorator
