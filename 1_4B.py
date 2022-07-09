import pandas as pd

filename = 'orderdata_sample.csv'

df = pd.read_csv(filename)
d2f=df.assign(Total = lambda x: round(x.Quantity * x.Price, 2) + x.Freight)

print(d2f)

d2f.to_csv('new_orderdata-sample.csv')
