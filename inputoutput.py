num = int(input("Enter first number\n"))
num1 = int(input("Enter Second Number\n"))
num2 = int(input("Enter Third Number\n"))
num3 = int(input("Enter Fourth Number\n"))
if num > num1 and num < num2:
    print("From the number given First, is the largest")
if num1 > num and num1 > num2:
    print("From the number given Second, is the largest")
if num2 > num and num2 > num1:
    print("From the number given Third, is the largest")
if num3 > num and num3 > num2:
    print("From the number given Fourth, is the largest")

