year = int(input("What year is it: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("It is a leap year!")
else:
    print("It is not a leap year!")