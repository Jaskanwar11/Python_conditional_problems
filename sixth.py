dist = int(input("How far is your destination(Kms): "))

if dist < 3:
    print("Go by your foot!")

elif dist < 15:
    print("Go by a bike!")

else:
    print("Go by a car!")