# train_model.py
import pickle
import pandas as pd
from sklearn import linear_model


def train_and_save_model(): # This is a dummy data to train the model, if you wish to add your other data you can add it here or can just read the csv file
    house_data = {
        "sizes": [1200, 1500, 1000, 1800, 1600],
        "bedrooms": [3, 4, 2, 4, 3],
        "prices": [250000, 320000, 180000, 350000, 270000],
    }

    df = pd.DataFrame(house_data)
    reg = linear_model.LinearRegression()
    reg.fit(df[["sizes", "bedrooms"]], df["prices"])

    with open("model.pkl", "wb") as f:
        pickle.dump(reg, f)

    print("Model saved")


if __name__ == "__main__":
    train_and_save_model()
