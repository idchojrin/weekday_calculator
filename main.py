from datetime import datetime

from week_day_calculator import week_day_for

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    date = input("Please enter the date (Y/m/d): ")
    print("Week day for: " + str(date) + " = " + week_day_for(datetime.strptime(date, '%Y/%m/%d')))
