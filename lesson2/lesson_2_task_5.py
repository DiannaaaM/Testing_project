def month_to_season(month: int) -> str:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[month-1]

some_month = int(input('Enter month: '))
print(month_to_season(some_month))