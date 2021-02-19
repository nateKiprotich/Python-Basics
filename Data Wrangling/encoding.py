import pandas as pd

headers = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',  'num-of-doors', 'body-style',  'drive-wheels', 'engine-location', 'wheel-base', 'length',   'width', 'height',   'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',   'compression-ratio',   'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
df = pd.read_csv('../Data/autos.csv', header=None)
df.columns = headers

pd.get_dummies(df['fuel-type'])

print(df.head())