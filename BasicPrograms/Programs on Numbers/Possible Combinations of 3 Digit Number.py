from itertools import permutations
num = int(input("Enter a 3 Digit Number: "))
lis = []
while num != 0:
    lis.append(num % 10)
    num //= 10
combination = permutations(lis, 3)
print("Possible Combinations of the 3 Digit Number")
for i in list(combination):
    print("".join(map(str, i)))
