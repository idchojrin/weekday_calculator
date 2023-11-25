import datetime


def week_day_for(date):
    current_date = datetime.datetime(2023, 10, 9)
    week_day = 1

    if date > current_date:
        while current_date < date:
            current_date = current_date + datetime.timedelta(days=1)
            week_day = week_day + 1
            if week_day == 8:
                week_day = 1
    else:
        while current_date > date:
            current_date = current_date - datetime.timedelta(days=1)
            week_day = week_day - 1
            if week_day == 0:
                week_day = 7

    if week_day == 1:
        return "Monday"
    elif week_day == 2:
        return "Tuesday"
    elif week_day == 3:
        return "Wednesday"
    elif week_day == 4:
        return "Thursday"
    elif week_day == 5:
        return "Friday"
    elif week_day == 6:
        return "Saturday"
    elif week_day == 7:
        return "Sunday"
    else:
        return "This isn't a past date: " + str(week_day)
