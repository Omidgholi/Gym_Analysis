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
        """This is a function that is called when the user clicks on the 'submit start range' button.
         It also creates and positions the 'submit end range button' and calls the 'get_date' function
         when the 'submit end range button' is clicked"""
        global end_cal
        global end_button
        start_button.config(state="disabled")
        end_cal = DateEntry(root, mindate=start_cal.get_date(), maxdate=date.today())
        end_cal.grid(pady=5)
        end_button = tk.Button(root, text="Submit End Range", command=get_date, font=6)
        end_button.grid(pady=5)


    def get_date():
        """This is a function that calls the select venue function. It is called when the user clicks the
         'submit end range button' and disables the button so the user cannot submit multiple ranges"""
        select_venue()
        end_button.config(state="disabled")


    def range_data():
        """This is a function that destroys the venue selection buttons and positions the start range button.
        This function is called when the user selects the 'select range' of dates button"""
        all_button.destroy()
        range_button.destroy()
        start_cal.grid(pady=5)
        start_button.grid(pady=5)


    def all_data():
        """This is a function that calls the select venue function and destroys the 'date range' button. This
        function is called when the user clicks the 'all-dates' button"""
        all_button.destroy()
        range_button.destroy()
        select_venue()


    def analysis():
        """This is a function that runs the analysis when the user clicks the 'submit' button after making
        a selection for date range and venue. This function is called within the select venue function"""
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
        tk.messagebox.showinfo(message="Report Successfully Saved to Output/Data.csv")


    def select_venue():
        """This is a function that provides the user with a dropdown list of the ARC venues for them to make a
        selection. It creates and positions a venue selection label, the 'submit' button to run the analysis, and
        an informational label that informs the user of what will happen upon clicking submit"""
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


    root = tk.Tk() # Initialise the root window
    root.title("ARC Gym Analysis")
    root.configure(bg="red2")
    greeting_label = tk.Label(text="Hello and Welcome to the...", bg="red2", fg="black", font=12)
    greeting_label.grid(pady=5)
    image = ImageTk.PhotoImage(Image.open("database/ARC_Image.png")) # Initialise the image
    serve_image = Label(root, image=image) # Label the image
    serve_image.grid() # Display the image

    gym_analyzer_label = tk.Label(text="ARC Gym Analyzer!", bg="red2", fg="black", font=12)
    gym_analyzer_label.grid(pady=5)

    range_selection_label = tk.Label(text="Please select either a range of dates or all dates for running analysis:", bg="red2", fg="black", font=8)
    range_selection_label.grid(pady=5)

    all_button = tk.Button(text="All Dates", command=all_data, bg="white", fg="black", font=6)
    range_button = tk.Button(text="Date Range", command=range_data, bg="white", fg="black", font=6)

    all_button.grid(pady=5)
    range_button.grid(pady=5)

    

    start_cal = DateEntry(root, maxdate=date.today()) # Initialise the start calendar

    start_button = tk.Button(text="Submit Start Range", command=serve_end_cal, font=6)

    root.mainloop()
