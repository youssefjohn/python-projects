def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    for day in days:
        yield day


days = week()
next(days)


def counting(x):
    count = 1
    while count < x:
        yield count
        count +=1


two = counting(5)
next(two)