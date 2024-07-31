day = input("What day is today: ")
age = int(input("Enter your age: "))

if age < 18:
    price = 8
else:
    price = 12 

if day.lower() == "wednesday":
    final_price = price - 2

else: 
    final_price = price

print("Price for you ticket will be: ", final_price, "Rupees!")