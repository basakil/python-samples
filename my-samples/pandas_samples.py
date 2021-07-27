import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('devops.csv')

print(f'\npandas returned type:{type(df)} ')
print(f'pandas returned columns types:\n{df.dtypes} ')
df.sort_values(by="Tarih", ascending=False)
print(df.head(5))