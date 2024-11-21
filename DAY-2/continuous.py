import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate data points for a normal distribution
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, loc=0, scale=1)  # Standard normal distribution

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='Normal Distribution')
plt.fill_between(x, y, where=(x >= -1) & (x <= 1), color='red', alpha=0.3)

# Add labels and title
plt.title('Continuous Probability: Standard Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.legend()

# Calculate probability for a specific interval (-1 to 1)
prob = stats.norm.cdf(1) - stats.norm.cdf(-1)
print(f"Probability of value being between -1 and 1: {prob:.4f}")

# Show the plot
plt.show()
