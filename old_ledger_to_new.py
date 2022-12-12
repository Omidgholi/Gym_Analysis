import pandas as pd

#df = pd.read_csv(r"/Users/omidgholizadeh/Documents/occupancy_data.csv")
#df = pd.concat(gdf.T for _, gdf in df.set_index(df.index % 3).groupby(df.index // 3))
#df.reset_index().to_csv("data_new.csv", index=False, header=False)

import csv
from itertools import islice

with open(r"/Users/omidgholizadeh/Documents/occupancy_data.csv", "r") as fin,\
     open("data_new.csv", "w") as fout:
    reader, writer = csv.reader(fin), csv.writer(fout)
    header = next(reader)
    length = len(header) - 1
    while (rows := list(islice(reader, length))):
        writer.writerows([first, *rest] for first, rest in zip(header, zip(*rows)))
