from sklearn.linear_model import LinearRegression
import numpy as np

def predict_population(data):
    if len(data) < 2:
        return "Not enough data"

    X = np.array(range(len(data))).reshape(-1, 1)
    y = np.array(data)

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[len(data)]])
    return int(prediction[0])