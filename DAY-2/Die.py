import random

def roll_die():
    """Simulates rolling a single 6-sided die"""
    return random.randint(1, 6)

def roll_two_dice():
    """Simulates rolling two 6-sided dice and returns their sum"""
    die1 = roll_die()
    die2 = roll_die()
    return die1 + die2

def analyze_rolls(num_rolls):
    """Analyzes statistics of multiple die rolls"""
    # Single die statistics
    single_rolls = [roll_die() for _ in range(num_rolls)]
    fours = sum(1 for roll in single_rolls if roll == 4)
    evens = sum(1 for roll in single_rolls if roll % 2 == 0)
    
    # Two dice statistics
    sums = [roll_two_dice() for _ in range(num_rolls)]
    sevens = sum(1 for roll in sums if roll == 7)
    
    print(f"\nResults from {num_rolls} rolls:")
    print(f"Rolling a 4: {fours} times ({(fours/num_rolls)*100:.1f}%)")
    print(f"Rolling an even number: {evens} times ({(evens/num_rolls)*100:.1f}%)")
    print(f"Rolling a sum of 7 with two dice: {sevens} times ({(sevens/num_rolls)*100:.1f}%)")

# Test with 1000 rolls
analyze_rolls(10)
