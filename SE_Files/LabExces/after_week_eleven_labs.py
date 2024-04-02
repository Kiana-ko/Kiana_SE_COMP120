# Week 11


# Exercise 1
# Import the correct library and print a calendar for your project. Print October month calendar of this year
# sample output as follows :
# may in calender format

import calendar
import datetime

yy = 2024
mm = 10
print(f"Current month rn:\n")
print(calendar.month(yy, mm))

current_date = datetime.date.today()

date_rn = current_date.strftime("%B %d, %Y")
print(f"Current date and time is:\nCurrent date: {date_rn}")

current_time = datetime.datetime.now().time()
formatted_current_time = current_time.strftime("%H:%M:%S")
print(f"Current time: {formatted_current_time}")

'''
Exercise 2 
Use 5 Functions in Python Math Module  and print the results 
'''
