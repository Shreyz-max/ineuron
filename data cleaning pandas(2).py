import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'],
 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
 'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
 'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
 '12. Air France', '"Swiss Air"']})

for i in range(len(df)):
    if pd.isna(df['FlightNumber'][i]):
        df.loc[i, 'FlightNumber'] = df.loc[i-1, 'FlightNumber'] + float(10)

df[['From', 'To']] = df.From_To.str.split('_', expand=True)
df['FlightNumber'] = df['FlightNumber'].astype(int)

def camel_case(x):
    return x[0].upper() + x[1:].lower()


df['From'] = df['From'].apply(camel_case)
df['To'] = df['To'].apply(camel_case)
df = df.drop(['From_To'], axis=1)


def joinlist(x):
    seq = ''
    for element in x:
        seq = seq + str(element) +','
    return seq.strip(',')


df['RecentDelays'] = df['RecentDelays'].apply(joinlist)
df = df.join(df['RecentDelays'].str.split(',', expand=True).add_prefix('delay_')).fillna(np.nan)
df = df.drop('RecentDelays', axis=1)
print(df)