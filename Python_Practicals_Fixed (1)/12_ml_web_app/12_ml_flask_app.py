"""Practical 12 - Mini data science application: data -> ML model -> Flask API.

Objectives
  * Data collection and processing
  * Data visualisation
  * Machine learning model building
  * API development using Flask / Flask-RESTful style endpoints

Needs data.csv with columns `Feature` and `target`. If missing, sample data is
generated. Local run:  python 12_ml_flask_app.py   then open http://127.0.0.1:5000/
Predict:         http://127.0.0.1:5000/predict?feature=6
"""
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).parent if "__file__" in globals() else Path.cwd()  # works in scripts and Colab/Jupyter
CSV_PATH = BASE_DIR / "data.csv"


def load_data(path=CSV_PATH):
    if path.exists():
        df = pd.read_csv(path)
    else:
        print(f"[note] {path.name} not found - using generated sample data.")
        rng = np.random.default_rng(0)
        feature = np.arange(1, 51)
        df = pd.DataFrame({"Feature": feature, "target": 3 * feature + 5 + rng.normal(0, 4, 50)})
    return df.dropna()


def train_model(df):
    # scikit-learn needs a 2-D X: use double brackets. (Original names x-train / x-test
    # also had hyphens, which are not valid Python identifiers.)
    X = df[["Feature"]]
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Model trained successfully")
    print(f"R^2 on test data: {model.score(X_test, y_test):.3f}")
    return model


df = load_data()
print(df.head())
model = train_model(df)

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Data Science API"


@app.route("/predict")
def predict():
    try:
        feature = float(request.args["feature"])
    except (KeyError, ValueError):
        return jsonify(error="Provide a numeric ?feature= query parameter"), 400
    prediction = model.predict(pd.DataFrame({"Feature": [feature]}))[0]
    return jsonify(feature=feature, prediction=round(float(prediction), 3))


def show_plot():
    df.hist()
    plt.tight_layout()
    plt.show()


def in_colab():
    return "google.colab" in sys.modules


if __name__ == "__main__":
    if in_colab():
        # Colab can't open http://127.0.0.1:5000 in your browser, so exercise the
        # same routes with Flask's built-in test client instead of starting a server.
        client = app.test_client()
        print("GET /               ->", client.get("/").get_data(as_text=True))
        print("GET /predict?feature=6 ->", client.get("/predict?feature=6").get_json())
        show_plot()
    else:
        if os.environ.get("SHOW_PLOT"):
            show_plot()
        app.run(debug=True)  # debug is fine in a lab; never use it in production
