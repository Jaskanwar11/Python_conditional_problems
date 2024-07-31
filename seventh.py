size = input("What would you prefer\n1.large\n2.medium\n3.small\n")

esp = input("Would you like an extra shot of espresso: ")

if esp.lower() == "yes":
    print("Your order is one", size, "coffee with extra shot of espresso")
else:
    print("Your order is one", size, "coffee")
