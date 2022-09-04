num = int(input("Enter the Number: "))
sumNum = 0
for i in range(1, num):
    if num % i == 0:
        sumNum += i
if num == sumNum:
    print("{} is a Perfect Number".format(num))
else:
    print("{} is not a Perfect Number".format(num))
