import pandas as pd

df = pd.read_csv("booksummaries.csv", nrows=1)

print (df.to_string())