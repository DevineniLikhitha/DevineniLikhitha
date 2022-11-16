

import pandas as pd

#csv1 = pd.read_excel('KW_Attributes.xlsx')
#csv2 = pd.read_excel('KW_Performance_L120D.xlsx')
#merged = csv1.merge(csv2, on='KW ID')
#merged.to_excel("output1.xlsx", index=False)

df = pd.read_excel('output1.xlsx')

#df["MKT"] = df["Campaign"].str.split("-").str[1]
#df['MKT'] = df['Campaign'].str.slice(7, 10)


df['MK'] = df['Ad group'].map(lambda x: x.lstrip('_-').rstrip('SRCH'))
df.to_excel("output1.xlsx")