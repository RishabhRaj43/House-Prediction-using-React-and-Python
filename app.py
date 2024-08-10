import pickle

import pandas as pd
from flask_cors import CORS

from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app)


@app.route("/api/predict/", methods=["POST"])
def index():
    data = request.json
    sizes = data["sizes"]
    bedrooms = data["bedrooms"]
    # print(sizes, bedrooms)

    new_data = pd.DataFrame({"sizes": sizes, "bedrooms": bedrooms})

    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    prices = model.predict(new_data).tolist()
    results = []

    for size, bedroom, price in zip(sizes, bedrooms, prices):
        results.append(
            {
                "size": size,
                "bedroom": bedroom,
                "predicted_price": f"{price : ,.2f}",
            }
        )

    return jsonify({"message": "Prediction results", "results": results})


if __name__ == "__main__":
    host = "localhost" # Add this or your app will not run
    port = "Your port number" # Add this port or your app will not run
    print(f"Running on http://{host}:{port}/")
    app.run(debug=True, host=host, port=port)
