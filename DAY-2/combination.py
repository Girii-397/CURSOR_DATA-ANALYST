def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
    # Formula for combination: C(n,r) = n! / (r! * (n-r)!)
    if n < r:
        return "Error: n must be greater than or equal to r"
    return factorial(n) // (factorial(r) * factorial(n - r))

# Example usage
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

result = combination(n, r)
print(f"C({n},{r}) = {result}")
