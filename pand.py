import pandas as pd
import csv
import time

import pandas as pd

df = pd.read_csv(r"/Users/omidgholizadeh/Documents/occupancy_data.csv", header=None).drop_duplicates()
# Read dataframe without header

# Create an empty DataFrame to store transposed data
tr = pd.DataFrame()

# Create, transpose and append subsets to new DataFrame
for i in range(1,df.shape[0],3):
    try:
        temp = pd.DataFrame()
        temp = temp.append(df.iloc[0])
        temp = temp.append(df.iloc[i:i+3])
        temp = temp.transpose()
        temp.columns = [0,1,2,3]
        tr = df.append(temp)
    except:
        pass

print(tr.to_csv("zolo.csv", index=False, header=False))