def is_year_leap(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

print(f'Год 2020: {is_year_leap(2020)}')