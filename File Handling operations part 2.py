# Step 1: Create and write into file
file = open(r"C:\Users\User\Downloads\sample_student.txt", "w")
file.write("Name: Ali\n")
file.write("Class: 10\n")
file.write("Subject: Computer Science\n")
file.close()

# Step 2: Read the file
file = open(r"C:\Users\User\Downloads\sample_student.txt", "r")
print("Reading File:\n")
print(file.read())
file.close()

# Step 3: Append new data
file = open(r"C:\Users\User\Downloads\sample_student.txt", "a")
file.write("Grade: A\n")
file.close()

# Step 4: Read again after append
file = open(r"C:\Users\User\Downloads\sample_student.txt", "r")
print("\nAfter Appending:\n")
print(file.read())
file.close()