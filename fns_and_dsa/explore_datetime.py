from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date

print(f"Current date and time: {display_current_datetime()}")

def calculate_future_date():
    day = int(input("Enter the number of days to add to the current date: "))
    future_date = display_current_datetime() + timedelta(days = day)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

calculate_future_date()

