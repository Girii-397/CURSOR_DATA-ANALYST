# Calculate probabilities for coin flips

# Initial conditions
possible_outcomes = 2  # Heads and Tails

print("Probability Analysis for a Fair Coin:")
print("-" * 35)

# For a fair coin, probability of heads = probability of tails = 1/2
print("\nFor a fair coin:")
print(f"Probability of getting Heads: 1/{possible_outcomes}")
print(f"Probability of getting Tails: 1/{possible_outcomes}")

# Some additional probability scenarios
print("\nOther probability scenarios:")

# Probability of getting either heads or tails (certainty)
print(f"Probability of getting either Heads or Tails: {possible_outcomes}/{possible_outcomes}")

# Probability of getting heads in two consecutive flips
consecutive_heads = f"1/{possible_outcomes * possible_outcomes}"  # 1/4
print(f"Probability of getting two consecutive Heads: {consecutive_heads}")

# Note: These probabilities assume a fair coin where both outcomes are equally likely
