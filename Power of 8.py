num = int(input("Enter a number: "))

while num % 8 == 0 and num > 1:
    num = num // 8

if num == 1:
    print("Power of 8")
else:
    print("Not a power of 8")