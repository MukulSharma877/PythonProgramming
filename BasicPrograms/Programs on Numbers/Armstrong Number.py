num = int(input("Enter a 3 or 2 Digit Number: "))
sumNum = 0
temp = num
while num != 0:
    rem = num % 10
    sumNum += (rem ** 3)
    num //= 10
if sumNum == temp:
    print("{} is an Armstrong Number".format(temp))
else:
    print("{} is not an Armstrong Number".format(temp))
