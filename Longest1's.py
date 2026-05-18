def max_consecutive_ones(n):
    count = 0
    while n > 0:
        # Bitwise AND with its own right-shifted version
        # This removes the trailing '1' from every cluster of 1s in each step
        n = n & (n << 1)
        count += 1
    return count

# Example usage:
number = 156  # Binary: 10011100
print(f"The longest consecutive 1s: {max_consecutive_ones(number)}")