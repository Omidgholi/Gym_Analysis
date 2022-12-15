import pandas as pd
cols = ["venue", "date", "time", "status", "count"]

df_new = pd.read_csv("occupancy_data_new.csv",names=cols)

df_new["venue"] = df_new["venue"].replace(['ARC Floor 1'], 'Arc Floor One')
df_new["venue"] = df_new["venue"].replace(["ARC Olympic Lifting Zones"], 'Arc Olympic Lifting Zones')
df_new["venue"] = df_new["venue"].replace(['ARC Floor 2'], 'Arc Floor Two')
df_new["venue"] = df_new["venue"].replace(['4 Court Gym'], 'Four Court Gym')
df_new["venue"] = df_new["venue"].replace(['ARC Express'], 'Arc Express')

df_old = pd.read_csv("database/database.csv", names=cols)

pd.concat([df_old, df_new]).to_csv("database/database.csv", index=False, header=False)
print("Done")