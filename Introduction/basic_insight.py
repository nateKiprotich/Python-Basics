import pandas as pd

headers = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',  'num-of-doors', 'body-style',  'drive-wheels', 'engine-location', 'wheel-base', 'length',   'width', 'height',   'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',   'compression-ratio',   'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
df = pd.read_csv('../Data/autos.csv', header=None)
df.columns = headers

# Checking data types of records
print(df.dtypes)
print(120*'-')

# Quick statistics - Numerical rows only
print(df.describe())

print(120*'-')

# Full summary statistics - All columns in the data frame
print(df.describe(include="all"))

print(120*'-')

# prints information about a DataFrame including the index dtype and columns, non-null values and memory usage
print(df.info())

