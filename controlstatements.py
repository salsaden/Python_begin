num1 = 45
num2 = 45
if num1 < num2:
    print("Num1 is less than Num2")
elif num1 == num2:
    print("num1 and num2 are equal")

salma = 29
stacy = 29
erick = 56
if salma > stacy and erick < stacy:
    print("Salma is the oldest")
elif salma == stacy or salma < erick:
    print("They are age mates")
elif salma < stacy:
    print("Salma is the youngest")
else:
    print("Error")
