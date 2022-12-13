import datetime
import tkinter as tk
from tkinter import *
import main

def get_age():
    global month, day, year
    year = year.get()
    month = month.get()
    month = month_options[month]
    day = day.get()

    age_root.destroy()

    age_in_years = ((datetime.date.today()-datetime.date(year=year, month=month, day=day)).days/365.25)

    if age_in_years < 18:
        tk.messagebox.showerror(message="You must be 18 years or older to use this application")
    else:
        main.main()



age_root = tk.Tk()
age_root.title("Age Verification")
month_options = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
                 "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

day_options = [i for i in range(1, 32)]
year_options = [i for i in range(1900, datetime.date.today().year)]

year = IntVar(age_root)

year.set("Year")

month = StringVar(age_root)
month.set("Month")

day = IntVar(age_root)
day.set("Day")

age_label = tk.Label(age_root, text="Please enter your date of birth to verify your age:")
age_label.grid(row=0, column=1, padx=5, pady=10)

day_dropdown = tk.OptionMenu(age_root, day, *day_options)
day_dropdown.grid(row=1, column=0, padx=5, pady=20)
month_dropdown = tk.OptionMenu(age_root,month, *month_options.keys())
month_dropdown.grid(row=1, column=1, padx=5, pady=20)
year_dropdown = tk.OptionMenu(age_root, year, *year_options)
year_dropdown.grid(row=1, column=2, padx=5, pady=20)


age_submit_button = tk.Button(age_root, text="Submit", command=get_age)
age_submit_button.grid(row=2, column=1, padx=20, pady=10)

age_root.mainloop()




