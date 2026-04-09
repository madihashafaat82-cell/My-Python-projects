def multiply_constant(N, M):
    """
    Method 1: 1 Iteration (O(1) - Constant Time)
    Uses the built-in multiplication operator.
    """
    return N * M

def multiply_iterative(N, M):
    """
    Method 2: N Iterations (O(N) - Linear Time)
    Simulates multiplication by adding M to a total, N times.
    """
    result = 0
    for i in range(N):
        result += M
    return result

# --- Testing the functions ---
n_val = 5
m_val = 10

print(f"Multiplying {n_val} and {m_val}:")
print(f"Constant Time Result: {multiply_constant(n_val, m_val)}")
print(f"Iterative Time Result: {multiply_iterative(n_val, m_val)}")