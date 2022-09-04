def fact(x):
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
    return factorial

num = int(input("Enter a Number: "))
temp = num
sumNum = 0
while num != 0:
    rem = num % 10
    sumNum += fact(rem)
    num //= 10
if sumNum == temp:
    print("{} is a Strong Number".format(temp))
else:
    print("{} is not a Strong Number".format(temp))
