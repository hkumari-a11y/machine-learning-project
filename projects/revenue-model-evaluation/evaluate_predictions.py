"""Evaluate fictional revenue predictions; no real RAFT records included."""
from math import sqrt
from statistics import median

ACTUAL = [100.0, 200.0, 400.0, 500.0, 900.0]
PREDICTIONS = {
    "baseline": [300.0] * 5,
    "illustrative_ols": [130.0, 250.0, 380.0, 570.0, 700.0],
    "illustrative_knn": [120.0, 220.0, 350.0, 540.0, 600.0],
}


def metrics(actual, predicted):
    if not actual or len(actual) != len(predicted):
        raise ValueError("actual and predicted must have equal nonzero length")
    errors = [abs(a - p) for a, p in zip(actual, predicted)]
    return {
        "mae": sum(errors) / len(errors),
        "median_ae": median(errors),
        "rmse": sqrt(sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)),
    }


if __name__ == "__main__":
    for name, predictions in PREDICTIONS.items():
        result = metrics(ACTUAL, predictions)
        print(name, " ".join(f"{key}={value:.2f}" for key, value in result.items()))
    assert metrics([1, 3], [2, 2])["mae"] == 1.0
