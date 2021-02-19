import pandas as pd

headers = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',  'num-of-doors', 'body-style',  'drive-wheels', 'engine-location', 'wheel-base', 'length',   'width', 'height',   'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',   'compression-ratio',   'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
df = pd.read_csv('../Data/autos.csv', header=None)
df.columns = headers

# Convert miles per gallon into litres per 100km
df["city-mpg"] = 235/ df["city-mpg"]

# rename column as below
df.rename(columns={"city-mpg": "city-L/100KM"}, inplace=True)

print(df["city-L/100KM"])
# print(df.dtypes)

# df["price"] = df["price"].astype("int")