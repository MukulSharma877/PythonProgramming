lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
count = 1
while (count ** 2) < upper:
    if (count ** 2) < lower:
        count += 1
    else:
        print(count ** 2, end = "\t")
        count += 1
