import pandas as pd
import numpy as np

headers = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',  'num-of-doors', 'body-style',  'drive-wheels', 'engine-location', 'wheel-base', 'length',   'width', 'height',   'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',   'compression-ratio',   'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
df = pd.read_csv('../Data/autos.csv', header=None)
df.columns = headers

"""
    axis=0  - Drops entire row
    axis=1  - Drops entire column
"""
print(df["price"].count())

df.dropna(subset=["price"], axis=0, inplace=True)

# Replace -
# mean = df["normalized-losses"].mean()
# df["normalized-losses"].replace(np.nan, mean)
