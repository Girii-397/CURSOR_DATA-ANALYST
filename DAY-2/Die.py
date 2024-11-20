# Calculate probabilities of rolling a fair six-sided die

# Initial conditions
sides = 6

# Theoretical probability for each number (always 1/6 for a fair die)
print("Probability Analysis for a Fair Six-Sided Die:")
print("-" * 45)
print("\nFor any number on the die:")
print(f"Probability = 1/{sides}")

# Calculate specific probabilities for different scenarios
print("\nSome example probability calculations:")

# Probability of rolling an even number (2,4,6)
even_outcomes = 3  # Count of favorable outcomes
print(f"\nProbability of rolling an even number: {even_outcomes}/{sides}")

# Probability of rolling a number greater than 4 (5,6)
greater_than_4 = 2  # Count of favorable outcomes
print(f"Probability of rolling a number greater than 4: {greater_than_4}/{sides}")

# Probability of rolling a number less than or equal to 3 (1,2,3)
less_equal_3 = 3  # Count of favorable outcomes
print(f"Probability of rolling a number less than or equal to 3: {less_equal_3}/{sides}")

# Probability of rolling a prime number (2,3,5)
prime_outcomes = 3  # Count of favorable outcomes
print(f"Probability of rolling a prime number: {prime_outcomes}/{sides}")

# Note: All these probabilities are based on a fair die where each outcome is equally likely

