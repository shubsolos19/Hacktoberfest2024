import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    # Check if either 5*n^2 + 4 or 5*n^2 - 4 is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Example usage
number = int(input("Enter a number: "))

if is_f
