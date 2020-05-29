import datetime

now = datetime.datetime.now()
current_year = now.year


age = int(input("Please enter your age (In number form ONLY): "))

years_til_hundered = 100 - age
year_hundered = current_year + years_til_hundered


print("You will be 100 in the year: ", year_hundered)

