import pandas as pd

df = pd.read_csv('../public/oasisctf.csv', low_memory=False)

flag = df.sort_values(by='TUNE', ascending=False).head(13)
print(''.join(flag.VAL.tolist()))
