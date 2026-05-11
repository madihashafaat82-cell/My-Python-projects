# Input number
n = int(input("Enter number: "))
res = 0

# Loop jab tak number khatam na ho jaye
while n > 0:
    res = (res << 1) | (n & 1)  # Naya bit shift karo aur add karo
    n >>= 1                     # Original number ka last bit hata do

print("Result:", res)