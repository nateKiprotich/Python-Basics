import pandas as pd
import numpy as np

headers = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',  'num-of-doors', 'body-style',  'drive-wheels', 'engine-location', 'wheel-base', 'length',   'width', 'height',   'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',   'compression-ratio',   'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
df = pd.read_csv('../Data/autos.csv', header=None)
df.columns = headers


df["price"] = df["price"].dropna()
df["price"] = df["price"].astype("int")

bins = np.linspace(min(df["price"]), max(df["price"]), 4)
group_names = ["Low", "medium", "High"]

df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True)