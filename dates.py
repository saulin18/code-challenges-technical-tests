import datetime
import calendar
from calendar import monthcalendar, monthrange
from nt import truncate
import time
import dateutil
# Table of contents
# Exercise 1: Print Current Date and Time
# Exercise 2: Convert String Into Datetime Object
# Exercise 3: Subtract a Week From a Given Date
# Exercise 4: Format DateTime
# Exercise 5: Find Day of Week
# Exercise 6: Add Week to Given Date
# Exercise 7: Print Current Time in Milliseconds
# Exercise 8: Convert Datetime into String
# Exercise 9: Calculate the date 4 months from the current date
# Exercise 10: Calculate Days Between Two Dates
# Exercise 1: Print Current Date and Time


def print_current_datetime():
    now = datetime.datetime.now()
    print("Current date and time: ")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


print_current_datetime()

# Exercise 2: Convert String Into Datetime Object\
# Write a code to convert the given date in string format into a Python DateTime object.
# date_string = "Feb 25 2020 4:20PM"
# Expected output:
# 2020-02-25 16:20:00


def convert_string_to_datetime(date_string):
    date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    return date_object

def add_months(date: datetime.datetime, months: int) -> datetime.datetime:
    year = date.year
    month = date.month + months
    
    # Ajustar año (funciona para positivos y negativos)
    if month > 12 or month < 1:
        year += (month - 1) // 12
        month = ((month - 1) % 12) + 1
    
    # Ajustar día si es inválido
    last_day = monthrange(year, month)[1]
    day = min(date.day, last_day)
    
    return datetime.datetime(year, month, day, date.hour,
                            date.minute, date.second, date.microsecond)

date_string = "2020-02-25 16:20:00"

print(convert_string_to_datetime(date_string))

# Exercise 3: Subtract a Week From a Given Date
# Write a code to subtract a week (7 days) from a given date.

# Given:
# given_date = datetime(2020, 2, 25)
# Expected output:
# 2020-02-


def subtract_week_from_date(given_date):
    new_date = given_date - datetime.timedelta(days=7)
    return new_date


given_date = datetime.datetime(2020, 2, 25)
print(subtract_week_from_date(given_date))

# Given:
# given_date = datetime(2020, 2, 25)
# Expected output:
# Tuesday 25 February 2020


def format_datetime(given_date: datetime.datetime) -> str:
    new_date = given_date.strftime("%A %d %B %Y")
    return new_date


given_date = datetime.datetime(2020, 2, 25)
print(format_datetime(given_date))

# Exercise 5: Find Day of Week
# Write a code to find the day of the week of a given date.
# Given:
# given_date = datetime(2020, 7, 26)
# Expected output:
# Sunday

# def find_day_of_week(given_date: datetime.datetime) -> str:
#    return given_date.strftime("%A")

# Using calendar module .get_day


def find_day_of_week(given_date: datetime.datetime) -> str:
    # given_date.weekday()
    day_index = calendar.weekday(given_date.year, given_date.month, given_date.day)
    return calendar.day_name[day_index]


given_date = datetime.datetime(2020, 7, 26)
print(find_day_of_week(given_date))

# Exercise 6: Add Week to Given Date
# Write a code to add a week (7 days) and 12 hours to a given date.
# Given:
## 2020-03-22 10:00:00
# given_date = datetime(2020, 3, 22, 10, 0, 0)
# Expected output:
# 2020-03-29 22:00:00

# def add_week_to_date(given_date: datetime.datetime) -> datetime.datetime:
#    new_date = given_date + datetime.timedelta(days=7)
#    return new_date

# Exercise 7: Print Current Time in Milliseconds

# def print_current_time_milliseconds():
#    timestamp = time.time()
#    milliseconds = int(timestamp * 1000)
#    return milliseconds


def print_current_time_milliseconds():
    date = datetime.datetime.now()
    milliseconds = datetime.datetime.timestamp(date) * 1000
    return int(milliseconds)


# Exercise 8: Convert Datetime into String
# Write a code to convert a given datetime object into a string.
#
# Given:
#
# given_date = datetime(2020, 2, 25)
# Expected output:
#
# "2020-02-25 00:00:00"

# def convert_datetime_to_string(given_date: datetime.datetime) -> str:
#    return given_date.strftime("%Y-%m-%d %H:%M:%S")

# Given:
#
## 2020-02-25
# given_date = datetime(2020, 2, 25).date()
# Expected Output:
#
# 2020-06-25


def add_four_months_to_date(given_date: datetime.datetime) -> datetime.datetime:
    time_delta = dateutil.relativedelta.relativedelta(months=4)
    return given_date + time_delta


given_date = datetime.datetime(2020, 2, 25)
print(add_four_months_to_date(given_date))

# Exercise 10: Calculate Days Between Two Dates
# Write a code to calculate the days between two dates.
# Refer: Python Difference Between Two Dates in Days.
# Given:
## 2020-02-25
# date_1 = datetime(2020, 2, 25)
## 2020-09-17
# date_2 = datetime(2020, 9, 17)


def calculate_days_between_dates(
    date_1: datetime.datetime, date_2: datetime.datetime
) -> int:
    difference = date_2 - date_1
    return difference.days


date_1 = datetime.datetime(2020, 2, 25)
date_2 = datetime.datetime(2020, 9, 17)
print(calculate_days_between_dates(date_1, date_2))

# def print_all_the_sundays_given_year(year: int) -> list[datetime.date]:
#    sundays = []
#
#    for month in range(1, 13):
#        cal = calendar.monthcalendar(year, month)
#        for week in cal:
#            if week[calendar.SUNDAY] != 0:
#                sundays.append(datetime.date(year, month, week[calendar.SUNDAY]))


def print_all_the_sundays_given_year(year: int) -> list[datetime.date]:
    sundays = []
    for month in range(1, 13):
        month_calendar = monthrange(year, month)
        num_days = month_calendar[1]
        for day in range(1, num_days + 1):
            if datetime.date(year, month, day).weekday() == calendar.SUNDAY:
                sundays.append(datetime.date(year, month, day))

    return sundays


def get_num_days_given_month_and_year(month: int, year: int) -> int:
    month_calendar = monthrange(year, month)
    num_days = month_calendar[1]
    return num_days


# Count first mondays of one year to other
# 24. Count First Mondays
#
# Write a Python program to count the number of Mondays on the 1st day of the month from 2015 to 2016.

# def count_first_mondays(start_year: int, end_year: int) -> int:
#    count = 0
#    for year in range(start_year, end_year + 1):
#        for month in range(1, 13):
#            if datetime.date(year, month, 1).weekday() == calendar.MONDAY:
#                count += 1
#    return count


def count_first_mondays(start_year: int, end_year: int) -> int:
    count = 0
    time_delta_first_monday = dateutil.relativedelta.relativedelta(
        weekday=calendar.MONDAY(+1)
    )
    time_delta_increase_month = dateutil.relativedelta.relativedelta(months=1)
    current = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    while current <= end_date:
        # Start counting
        next_monday = current + time_delta_first_monday

        if next_monday.day == 1:
            count += 1

        current += time_delta_increase_month

    return count

#import datetime
#import calendar
#
#def count_first_mondays(start_year: int, end_year: int) -> int:
#    count = 0
#    for year in range(start_year, end_year + 1):
#        for month in range(1, 13):
#            first_day = datetime.date(year, month, 1)
#            if first_day.weekday() == calendar.MONDAY:
#                count += 1
#    return count

# Next birth-day of the week finder
# Can you find after how many years will a person's birthday fall on the same day of the week that he was born?
# For example, Joy's birthday is on 16th October, 1990 which falls on Friday. A
# fter how many years will his birthday fall on Friday again? (That would be 11 years)
#
# Note
# Month is zero-indexed
# nextBirthdayOfTheWeek(new Date(1990, 9, 16)) //11
# nextBirthdayOfTheWeek(new Date(2012, 5, 20))  //6
# nextBirthdayOfTheWeek(new Date(1975, 2, 22))  //5
from datetime import datetime
from dateutil.relativedelta import relativedelta
from calendar import monthrange, monthcalendar


def next_birthday_date(birthday: datetime) -> int:
    week_day_of_birthday = birthday.weekday()

    delta_of_same_weekday = relativedelta(years=1)

    count_of_years = 0
    temp = birthday
    while truncate:
        count_of_years += 1
        temp += delta_of_same_weekday
        if temp.weekday() == week_day_of_birthday:
            return count_of_years

    return -1


#def next_birthday_date(birthday: datetime.datetime) -> int:
#    week_day_of_birthday = birthday.weekday()
#    count_of_years = 0
#    temp = birthday
#    
#   
#    max_years = 100
#    
#    while count_of_years < max_years:
#        count_of_years += 1
#       
#        try:
#         
#            temp = datetime.datetime(
#                temp.year + 1,
#                temp.month,
#                temp.day,
#                temp.hour,
#                temp.minute,
#                temp.second
#            )
#        except ValueError:
#            # Si el día no existe (ej: 29 de febrero), usar el último día del mes
#            from calendar import monthrange
#            last_day = monthrange(temp.year + 1, temp.month)[1]
#            temp = datetime.datetime(
#                temp.year + 1,
#                temp.month,
#                min(temp.day, last_day),
#                temp.hour,
#                temp.minute,
#                temp.second
#            )
#        
#        if temp.weekday() == week_day_of_birthday:
#            return count_of_years
#    
#    return -1
