x = int(input("Enter a number: "))
xstr = str(x)
if xstr[0] == xstr[-1]:        
    print("Paindrome")
else:
    print("not palindrome!")