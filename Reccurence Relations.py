def recurrence_function(n):
    # Base Case: Agar n 0 ya us se chota ho jaye toh ruk jao
    if n <= 0:
        return
    
    # Kaam: "Yes" print karna
    print(f"Current n: {n} -> Output: Yes")
    
    # Recursive Calls: Function apne aap ko n/2 ke sath call kar raha hai
    # Ye asli recursion hai
    recurrence_function(n // 2)
    recurrence_function(n // 2)

# Function ko call karna
print("--- Starting Recursion ---")
recurrence_function(4)