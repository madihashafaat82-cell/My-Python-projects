num = int(input("Enter a number: "))

rightmost_set_bit = num & -num

print("Rightmost set bit is:", rightmost_set_bit)