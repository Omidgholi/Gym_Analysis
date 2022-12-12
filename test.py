import pandas as pd

df = pd.read_csv(r"/Users/omidgholizadeh/Documents/occupancy_data.csv")


final=pd.concat([df[:4].set_index('Entry').T,df[4:].set_index('Entry').T])


final.to_csv("test1.csv")

