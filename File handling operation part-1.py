# Create a sample file first (so your program doesn't crash)
file = open(r"C:\Users\User\student.txt", "w")
file.write("Ali\nAhmed\nSara\nZain\n")
file.close()

# 1. Read full file
file = open(r"C:\Users\User\student.txt", "r")
print("Read full file:")
print(file.read())
file.close()

# 2. Read line by line
file = open(r"C:\Users\User\student.txt", "r")
print("Read line by line:")
for line in file:
    print(line.strip())
file.close()

# 3. Read first line only
file = open(r"C:\Users\Userstudent.txt", "r")
print("First line:")
print(file.readline())
file.close()