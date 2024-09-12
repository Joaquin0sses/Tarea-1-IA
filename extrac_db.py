import pandas as pd

size = 1000000
df_chunk = pd.read_csv('archive/test.csv', chunksize=size)

header = True

df_chunk[0].to_csv('db.csv', header=header, mode='a')



