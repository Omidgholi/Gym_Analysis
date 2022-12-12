from tkcalendar import DateEntry
from datetime import date
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import os
import statistics
import pandas as pd



def serve_end_cal():
    global end_cal
    global end_button
    start_button.config(state="disabled")
    end_cal = DateEntry(root, mindate=start_cal.get_date(), maxdate=date.today())
    end_cal.grid()
    end_button = tk.Button(root, text="Submit End Range", command=get_date)
    end_button.grid()


def get_date():
    select_venue()
    end_button.config(state="disabled")


def range_data():
    all_button.destroy()
    range_button.destroy()
    start_cal.grid()
    start_button.grid()


def all_data():
    all_button.destroy()
    range_button.destroy()
    select_venue()


def analysis():
    try:
        start_date = pd.to_datetime(start_cal.get_date(), infer_datetime_format=True, cache=True)
        end_date = pd.to_datetime(end_cal.get_date(), infer_datetime_format=True, cache=True)
    except:
        #start_date = pd.to_datetime("1/1/2000", infer_datetime_format=True)
        #end_date = pd.to_datetime("1/1/2070", infer_datetime_format=True)
        start_date = None
        end_date = None


    print(start_date, end_date)
    venue = clicked.get()
    print(venue)
    root.destroy()
    statistics.gym_analysis(venue, start_date, end_date)
    tk.messagebox.showinfo(message="Report Successfully Saved to Data.csv")


def select_venue():
    range_selection_label.destroy()
    venue_label = tk.Label(text="Please select a venue you would like to analyse from the options below", bg="red", fg="black")
    venue_label.grid()
    global clicked
    clicked = StringVar(root)
    clicked.set("ALL")
    venue_options = ["ALL","Entry","Arc Floor One", "Climbing", "Arc Olympic Lifting Zones", "Arc Floor Two",
                                     "South Court", "Four Court Gym", "North Court", "Recreation Pool", "Competition Pool",
                                     "Arc Express", "Spa", "Aquaplex Pool Deck", "Tennis Courts"]
    venue_select = OptionMenu(root, clicked, *venue_options)
    venue_select.grid()

    analysis_button = tk.Button(root, text="Submit", command=analysis)
    analysis_button.grid()
    analysis_label= tk.Label(root,text="*Clicking submit will run the analysis*", bg="red", fg="black")
    analysis_label.grid()


root = tk.Tk()
root.title("ARC Gym Analysis")
root.configure(bg="red")
greeting_label = tk.Label(text="Hello and Welcome to the...", bg="red", fg="black")
greeting_label.grid()
image = ImageTk.PhotoImage(Image.open("ARC_Image.png"))
serve_image = Label(root, image=image)
serve_image.grid()
date_label = tk.Label(text="How would you like to sort through the data?", bg="red", fg="black")
# range and all buttons
gym_analyzer_label = tk.Label(text="ARC Gym Analyzer!", bg="red", fg="black")
gym_analyzer_label.grid()

range_selection_label = tk.Label(text="Please select either a range of dates or all dates for running analysis:", bg="red", fg="black")
range_selection_label.grid()

all_button = tk.Button(text="All Dates", command=all_data, bg="red", fg="black")
range_button = tk.Button(text="Date Range", command=range_data, bg="red", fg="black")
# position on range buttons
all_button.grid()
range_button.grid()



start_cal = DateEntry(root, maxdate=date.today())

start_button = tk.Button(text="Submit Start Range", command=serve_end_cal)

root.mainloop()