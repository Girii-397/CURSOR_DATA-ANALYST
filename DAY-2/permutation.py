def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def permutation(n, r):
    # Formula for permutation: P(n,r) = n! / (n-r)!
    if n < r:
        return "Error: n must be greater than or equal to r"
    return factorial(n) // factorial(n - r)

# Example usage
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

result = permutation(n, r)
print(f"P({n},{r}) = {result}")
