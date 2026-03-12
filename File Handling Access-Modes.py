# File Handling Project

# Read Mode
file = open("student.txt", "r")
print("File in Read mode:")
print(file.read())
file.close()

# Write Mode (overwrite old content)
file = open("student.txt", "w")
file.write("File in Writing mode:")
file.write("6-Abdullah")
file.write("7-Shahid")
file.write("8-Shoaib")
file.write("9-Suleman")
file.close()

print("\nData written to file.")

# Append Mode (add new content)
file = open("student.txt", "a")
file.write("10-Salah")
file.close()

print("New data appended successfully.")

# Read Again
file = open("student.txt", "r")
print("\nUpdated File Content:")
print(file.read())
file.close()