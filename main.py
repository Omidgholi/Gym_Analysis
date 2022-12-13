from tkcalendar import DateEntry
from datetime import date
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import os
import statistics
import pandas as pd
import datetime

def main():
    def serve_end_cal():
        """This is a function that"""
        global end_cal
        global end_button
        start_button.config(state="disabled")
        end_cal = DateEntry(root, mindate=start_cal.get_date(), maxdate=date.today())
        end_cal.grid(pady=5)
        end_button = tk.Button(root, text="Submit End Range", command=get_date, font=6)
        end_button.grid(pady=5)


    def get_date():
        """This is a function that"""
        select_venue()
        end_button.config(state="disabled")


    def range_data():
        """This is a function that"""
        all_button.destroy()
        range_button.destroy()
        start_cal.grid(pady=5)
        start_button.grid(pady=5)


    def all_data():
        """This is a function that"""
        all_button.destroy()
        range_button.destroy()
        select_venue()


    def analysis():
        """This is a function that"""
        try:
            start_date = pd.to_datetime(start_cal.get_date(), infer_datetime_format=True, cache=True)
            end_date = pd.to_datetime(end_cal.get_date(), infer_datetime_format=True, cache=True)
        except:
            start_date = None
            end_date = None


        print(start_date, end_date)
        venue = venue_select.get()
        print(venue)
        root.destroy()
        statistics.gym_analysis(venue, start_date, end_date)
        tk.messagebox.showinfo(message="Report Successfully Saved to Data.csv")


    def select_venue():
        """This is a function that"""
        range_selection_label.destroy()
        venue_label = tk.Label(text="Please select a venue you would like to analyse from the options below:", bg="red2", fg="black", font=8)
        venue_label.grid(pady=5)
        global venue_select
        venue_select = StringVar(root)
        venue_select.set("ALL")
        venue_options = ["ALL","Arc Floor One", "Climbing", "Arc Olympic Lifting Zones", "Arc Floor Two",
                                         "South Court", "Four Court Gym", "North Court", "Recreation Pool", "Competition Pool",
                                         "Arc Express", "Spa", "Aquaplex Pool Deck", "Tennis Courts"]
        venue_menu = OptionMenu(root, venue_select, *venue_options)
        venue_menu.grid(pady=5)

        analysis_button = tk.Button(root, text="Submit", command=analysis, font=6)
        analysis_button.grid(pady=5)
        analysis_label= tk.Label(root,text="*Clicking submit will run the analysis*", bg="red2", fg="black", font=6)
        analysis_label.grid(pady=5)


    root = tk.Tk()
    root.title("ARC Gym Analysis")
    root.configure(bg="red2")
    greeting_label = tk.Label(text="Hello and Welcome to the...", bg="red2", fg="black", font=12)
    greeting_label.grid(pady=5)
    image = ImageTk.PhotoImage(Image.open("ARC_Image.png"))
    serve_image = Label(root, image=image)
    serve_image.grid()
    date_label = tk.Label(text="How would you like to sort through the data?", bg="red2", fg="black")

    gym_analyzer_label = tk.Label(text="ARC Gym Analyzer!", bg="red2", fg="black", font=12)
    gym_analyzer_label.grid(pady=5)

    range_selection_label = tk.Label(text="Please select either a range of dates or all dates for running analysis:", bg="red2", fg="black", font=8)
    range_selection_label.grid(pady=5)

    all_button = tk.Button(text="All Dates", command=all_data, bg="white", fg="black", font=6)
    range_button = tk.Button(text="Date Range", command=range_data, bg="white", fg="black", font=6)

    all_button.grid(pady=5)
    range_button.grid(pady=5)

    

    start_cal = DateEntry(root, maxdate=date.today())

    start_button = tk.Button(text="Submit Start Range", command=serve_end_cal, font=6)

    root.mainloop()
