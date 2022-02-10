from typing import Optional

import numpy as np
from flask import Flask, request

with open("./coefficients.csv", "r") as f:
    coefficients = [float(x.split(",")[1]) for x in f.readlines()[1::]]
    intercept = coefficients.pop(-1)
    coefficients = np.array(coefficients)

with open("./averages.csv", "r") as f:
    averages = np.array(
        [float(x.split(",")[1]) for x in f.readlines()[1::]])

app = Flask(__name__)
app.config["averages"] = averages
app.config["coefficients"] = coefficients
app.config["intercept"] = intercept


@app.route("/", methods=["POST"])
def get_score() -> dict[str, float]:
    j: dict[str, Optional[float]] = request.get_json()

    vals = list(j.values())
    for i, val in enumerate(vals):
        if val is None:
            vals[i] = app.config["averages"][i]

    coef = app.config["coefficients"]
    intercept = app.config["intercept"]

    score: float = np.dot(coef, vals).squeeze() + intercept
    return {"score": score}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
