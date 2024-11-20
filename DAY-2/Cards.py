import random

def draw_card():
    """Draws a random card from a standard 52-card deck"""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return f"{random.choice(ranks)} of {random.choice(suits)}"

def analyze_card_draws(num_draws):
    """Analyzes statistics of multiple card draws"""
    # Initialize counters
    hearts_count = 0
    face_cards = 0
    aces = 0
    
    # Perform draws
    for _ in range(num_draws):
        card = draw_card()
        if 'Hearts' in card:
            hearts_count += 1
        if any(face in card for face in ['Jack', 'Queen', 'King']):
            face_cards += 1
        if 'Ace' in card:
            aces += 1
    
    # Calculate probabilities
    hearts_prob = (hearts_count / num_draws) * 100
    face_prob = (face_cards / num_draws) * 100
    ace_prob = (aces / num_draws) * 100
    
    # Print results
    print(f"\nResults from {num_draws} card draws:")
    print(f"Hearts: {hearts_count} times ({hearts_prob:.1f}%)")
    print(f"Face cards: {face_cards} times ({face_prob:.1f}%)")
    print(f"Aces: {aces} times ({ace_prob:.1f}%)")
    print("\nTheoretical probabilities:")
    print(f"Hearts: 25.0%")
    print(f"Face cards: 23.1%")
    print(f"Aces: 7.7%")

# Test with 1000 draws
analyze_card_draws(10)
