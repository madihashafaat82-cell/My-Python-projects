num = int(input("Enter a number to check is this is an Arm strong number"))
order = len(str(num))
sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** order
    temp//=10


if sum_of_powers==num :
 print(num,' is an Arm strong number.')
else:
   print(num,' is not an Arm strong number.')