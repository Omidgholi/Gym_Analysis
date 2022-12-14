# Used paramaters such as venue, start_date, and end_date to generate statistical report regarding the ARC's Occupancy.
# Generates A CSV file with the output along with a graph to visualise the output.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import tkinter.messagebox
import tkinter as tk

def gym_analysis(venue, start_date, end_date):
    """Recieves the venue, start_date, and end_date from main.py and generates a statistical report regarding the ARC's Occupancy. """

    try:
        cols = ["venue", "date", "time", "status", "count"]
        df = pd.read_csv("database/database.csv", names=cols)  # Reads the database and stores it in a dataframe
        df["date"] = pd.to_datetime(df["date"], infer_datetime_format=True, cache=True, errors="coerce") # Converts the date column to datetime format
        df['time'] = pd.to_datetime(df['time'], infer_datetime_format=True, cache=True, errors="coerce").dt.hour # Converts the time column to datetime format and extracts the hour
        df["count"] = pd.to_numeric(df["count"], errors="coerce")  # Converts the count column to numeric format
    except:
        tk.messagebox.showerror(message="No Data Found") # If the database is not found, an error message is displayed
        exit()

    start_time = 0
    end_time = 24

    if start_date is None and end_date is None: # If the user selects all output, the start_date and end_date are set to None
        # Filters through the dataframe to find the output that matches the venue, time range, and status.
        if venue == "ALL":
            data = df[df["status"].eq("Open") & df['time'].between(start_time,end_time)]
        else:
            data = df[df["venue"].eq(venue) & df["status"].eq("Open") & df['time'].between(start_time, end_time)]
    else:
        try:
            if venue == "ALL":
                data = df[df["status"].eq("Open") & df["date"].between(start_date, end_date) & df['time'].between(start_time,end_time)]
            else:
                data = df[df["venue"].eq(venue) & df["status"].eq("Open") & df["date"].between(start_date, end_date) & df['time'].between(start_time, end_time)]
        except:
            tkinter.messagebox.showerror(message="Please Select a different date range", title="Error", icon="error") # If the user selects a date range that is not in the database, an error message is displayed
            exit()
    try:
        bottom_quartile = round(data["count"].quantile(0.25))  # Calculates the bottom quartile
        top_quartile = round(data["count"].quantile(0.75))  # Calculates the top quartile
        average = round(data["count"].mean())  # Calculates the average
        print(f"Venue: {venue}\nBottom Quartile: {bottom_quartile}\nAverage: {average}\nTop Quartile: {top_quartile}")
    except:
            tk.messagebox.showerror(message="No output available for this date range", title="Error", icon="error")  # Throws an error if the user selects a date range that is not in the database
            exit()


    ax = sns.lineplot(data=data, x="time", y="count", hue="venue", errorbar=None) # Plots the output
    ax.set(xlabel="Time (24h Format)", ylabel="Count") # Sets the x and y labels
    if start_date is None and end_date is None:
        ax.set_title(f"Occupancy Data for {venue}")
    else:
        ax.set_title(f"Occupancy Data for {venue} from {start_date} to {end_date}")
    plt.savefig("output/graph.png", pad_inches=0.5) # Saves the graph as a png file


    data = data.groupby(["time", "venue"]).mean(numeric_only=True).round(0).reset_index().sort_values(by="count") # Groups the output by time and venue and calculates the average
    data.to_csv("output/data.csv", index=False) # Saves the output as a csv file in output folder
