# This script verifies the age of the user. If the user is under 18, the program will exit.
import datetime
import tkinter as tk
from tkinter import *
import main
import webbrowser


def get_age():
    """Processes data obtained by age verification GUI.
     If the user is under 18, the program will exit"""
    try:
        global month, day, year  # global day, month, year
        year = year.get()
        month = month.get()
        month = month_options[month]
        day = day.get()

        age_root.destroy()  # Destroy the age root window
    # The calculated age in years is equal to today's date minus the date the user enters divided by 365.25
    # We used 365.25 to take into account leap years
        age_in_years = ((datetime.date.today()-datetime.date(year=year, month=month, day=day)).days/365.25)

        if age_in_years < 18:  # If the user enters a date that makes them less than 18 years old, an error message will appear
            tk.messagebox.showerror(message="You must be 18 years or older to use this application")
            try:
                webbrowser.open("https://en.caillou.com/", new=0, autoraise=True)
                exit()
            except:
                exit()
        else:  # If the user is above 18 years old
            main.main()  # Run main.py
    except:
        tk.messagebox.showerror(message="Please enter a valid date")
        exit()


age_root = tk.Tk()  # Create the tkinter window
age_root.title("Age Verification")  # Set the title of the window
# This is a dictionary that corresponds the month name key to an integer equivalent value
month_options = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
                 "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

day_options = [i for i in range(1, 32)]  # Provides day values from 1 to 31 for dropdown menu
year_options = [i for i in range(datetime.date.today().year, 1900, -1)]  # Descending year values from current year to 1900

year = IntVar(age_root)  # Initializing integer variable for year
year.set("Year")  # Setting dropdown title to Year

month = StringVar(age_root)  # Initializing integer variable for month
month.set("Month")  # Setting dropdown title to Month

day = IntVar(age_root)  # Initializing integer variable for day
day.set("Day")  # Setting dropdown title to Day

age_label = tk.Label(age_root, text="Please enter your date of birth to verify your age:")  # Instruction label
age_label.grid(row=0, column=1, padx=5, pady=10)  # Position for instruction label

day_dropdown = tk.OptionMenu(age_root, day, *day_options)  # Create the day dropdown menu using the day option for loop
day_dropdown.grid(row=1, column=0, padx=5, pady=20)  # Position for the day dropdown menu
month_dropdown = tk.OptionMenu(age_root,month, *month_options.keys())  # Create the month dropdown menu using month option dictionary
month_dropdown.grid(row=1, column=1, padx=5, pady=20)  # Position for the month dropdown menu
year_dropdown = tk.OptionMenu(age_root, year, *year_options)  # Create the year dropdown menu using year options for loop
year_dropdown.grid(row=1, column=2, padx=5, pady=20)  # Position for the year dropdown menu

# Create a "Submit" button that calls the "get_age" function
age_submit_button = tk.Button(age_root, text="Submit", command=get_age)
age_submit_button.grid(row=2, column=1, padx=20, pady=10)  # Position the age "Submit" button

age_root.mainloop()




