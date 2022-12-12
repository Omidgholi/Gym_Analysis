import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

cols = ["venue", "date", "time", "status", "count"]
df = pd.read_csv(r"/Users/omidgholizadeh/Documents/occupancy_data_new.csv",names=cols).drop_duplicates()

df["date"] = pd.to_datetime(df["date"], infer_datetime_format=True, cache=True, errors="coerce")
df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True, cache=True, errors="coerce").dt.hour


venue = "ALL"
start_date = "2020-01-01"
end_date = "2023-01-31"
start_time = 0
end_time = 24

try:
    if venue == "ALL":
        data = df[df["status"].eq("Open") & df["date"].between(start_date, end_date) & df['time'].between(start_time, end_time)]
    else:
        data = df[df["venue"].eq(venue) & df["status"].eq("Open") & df["date"].between(start_date, end_date) & df['time'].between(start_time, end_time)]
except:
    print("Error, Please try a different date range")
    exit()


bottom_quartile = round(data["count"].quantile(0.25))
top_quartile = round(data["count"].quantile(0.75))
average = round(data["count"].mean())
print(f"Bottom Quartile: {bottom_quartile}\nAverage: {average}\nTop Quartile: {top_quartile}")
bottom_quart = data[data["count"].between(bottom_quartile, top_quartile)]
# print(bottom_quart)




ax = sns.lineplot(data=data, x="time", y="count", hue="venue", ci=None)
ax.set(xlabel="Time", ylabel="Count")
ax.set_title(f"{venue} venues from {start_date} to {end_date} and {start_time}:00 to {end_time}:00")
# plt.legend(bbox_to_anchor=(1.01, 1), borderaxespad=0)
plt.show()
plt.savefig("test.png")