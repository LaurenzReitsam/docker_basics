from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import pandas as pd

if __name__ == "__main__":

    X, y = load_boston(return_X_y=True)

    lr = LinearRegression()
    lr.fit(X, y)

    coeff = lr.coef_.tolist()
    coeff.append(lr.intercept_)
    coeff = pd.Series(coeff, name="coefficients")
    coeff.to_csv("./coefficients.csv")

    means = pd.Series(X.mean(axis=0), name="averages")
    means.to_csv("./averages.csv")

