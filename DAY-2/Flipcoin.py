import random

def flip_coin():
    """Simulates flipping a fair coin and returns 'Heads' or 'Tails'"""
    if random.random() < 0.5:
        return "Heads"
    else:
        return "Tails"

def analyze_flips(num_flips):
    """Analyzes statistics of multiple coin flips"""
    # Track results
    heads_count = 0
    tails_count = 0
    
    # Perform flips
    for _ in range(num_flips):
        result = flip_coin()
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    
    # Calculate probabilities
    heads_prob = (heads_count / num_flips) * 100
    tails_prob = (tails_count / num_flips) * 100
    
    # Print results
    print(f"\nResults from {num_flips} coin flips:")
    print(f"Heads: {heads_count} times ({heads_prob:.1f}%)")
    print(f"Tails: {tails_count} times ({tails_prob:.1f}%)")
    print(f"Expected probability for each: 50.0%")

# Test with 1000 flips
analyze_flips(10)
