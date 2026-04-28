from math import sqrt

print("2-Digit Prime Numbers are:")

# 2-digit numbers start from 10 and end at 99
for num in range(10, 100):
    is_prime = True
    
    # Check factors from 2 up to square root of num
    for k in range(2, int(sqrt(num)) + 1):
        if (num % k) == 0:
            is_prime = False
            break
            
    if is_prime:
        print(num, end=" ")