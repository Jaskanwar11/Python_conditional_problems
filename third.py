math = int(input("Marks obtained in maths: "))
physics = int(input("Marks obtained in physics: "))
chemitry = int(input("Marks obtained in chemitry: "))
english = int(input("Marks obtained in english: "))
CS = int(input("Marks obtained in CS: "))

total_marks = math + physics + chemitry + english + CS
percentage = (total_marks/500) * 100
print("Total marks obtained: ",total_marks)
print("Percentage: ",percentage)

if percentage < 60:
    print("You got F grade")
elif percentage < 70:
    print("You got D grade")
elif total_marks < 80:
    print("You got C grade")
elif percentage < 90:
    print("You got B grade")
else:
    print("You got A grade")