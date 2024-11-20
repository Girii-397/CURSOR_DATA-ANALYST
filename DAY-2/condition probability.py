import random

def simulate_events(num_trials):
    """Simulates two dependent events and calculates conditional probability"""
    # Event A: Drawing a heart
    # Event B: Drawing a face card (given that we drew a heart)
    
    hearts_count = 0  # Total hearts drawn
    heart_face_count = 0  # Face cards among hearts
    
    for _ in range(num_trials):
        # Simulate drawing a card
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        
        suit = random.choice(suits)
        rank = random.choice(ranks)
        
        # Check if it's a heart
        if suit == 'Hearts':
            hearts_count += 1
            # Check if it's also a face card
            if rank in ['Jack', 'Queen', 'King']:
                heart_face_count += 1
    
    # Calculate probabilities
    p_heart = hearts_count / num_trials
    p_face_given_heart = heart_face_count / hearts_count if hearts_count > 0 else 0
    
    # Print results
    print(f"\nResults from {num_trials} trials:")
    print(f"Probability of drawing a heart: {p_heart:.3f}")
    print(f"Probability of drawing a face card, given that it's a heart: {p_face_given_heart:.3f}")
    print("\nTheoretical probabilities:")
    print(f"P(Heart) = 0.250")
    print(f"P(Face|Heart) = 0.231")

# Run simulation with 1000 trials
simulate_events(10)
