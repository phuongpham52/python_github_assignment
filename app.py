hours = input("How many hours did you study today? ")
#Convert the input into a numeric type (e.g., float) and perform at least one calculation.
hours = float(hours)
weekly_hours = hours * 7
print(f"You are on track to study {weekly_hours} hours this week.")
#basic error handling to prevent the program from crashing if the user enters a non-numeric value.
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()