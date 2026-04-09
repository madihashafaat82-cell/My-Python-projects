def calculate_sum(n):
    total = 0
    # This loop runs 'n' times, making it O(n) complexity
    for i in range(n):
        total += i
    return total

# Example usage:
n = 100
print(f"Time Complexity: O(n) for input size {n}")
print(f"Result: {calculate_sum(n)}")