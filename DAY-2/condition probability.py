# Calculate conditional probability of drawing a red ball given certain conditions

# Initial conditions
total_balls = 5
red_balls = 2
blue_balls = 3

# First draw: Probability of drawing a red ball
prob_first_red = red_balls/total_balls

# Second draw (without replacement): 
# Probability of drawing another red ball GIVEN that first ball was red
prob_second_red_given_first_red = (red_balls - 1)/(total_balls - 1)

# Calculate conditional probability as a fraction
conditional_probability = f"{red_balls - 1}/{total_balls - 1}"

print(f"Probability of first red ball: {red_balls}/{total_balls}")
print(f"Conditional probability of second red ball given first was red: {conditional_probability}")
# This will output: 
# Probability of first red ball: 2/5
# Conditional probability of second red ball given first was red: 1/4

