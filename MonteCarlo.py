import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SPINS = 1000000
STARTING_BANKROLL = 1000
BET_AMOUNT = 1

# American Roulette Wheel: 38 slots (1-36, 0, 00)
# Red numbers and black numbers
RED_NUMBERS = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
BLACK_NUMBERS = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

# Simulation Results
red_hits = 0
black_hits = 0
double_hits = 0
zero_hits = 0
high_hits = 0
low_hits = 0
even_hits = 0
odd_hits = 0
number_hits = {i: 0 for i in range(37)}  # 0-36 (37 numbers, including 0)
bankroll_red = 1000
bankroll_black = 1000
bankroll_alternating = 1000

# Track bankroll over time
bankroll_red_tracker = [bankroll_red]
bankroll_black_tracker = [bankroll_black]
bankroll_alternating_tracker = [bankroll_alternating]

# Alternating bet color
alternating_color = 'red'

for spin in range(NUM_SPINS):
    # Spin the wheel
    outcome = np.random.randint(0, 38)  # 0-36, 37 represents '00'

    # Update counts
    if outcome in RED_NUMBERS:

        red_hits += 1
        bankroll_red += BET_AMOUNT
        bankroll_black -= BET_AMOUNT

        if alternating_color == 'red':
            bankroll_alternating += BET_AMOUNT
        else:
          bankroll_alternating -= BET_AMOUNT

    elif outcome in BLACK_NUMBERS:

        black_hits += 1
        bankroll_black += BET_AMOUNT
        bankroll_red -= BET_AMOUNT

        if alternating_color == 'black':
            bankroll_alternating += BET_AMOUNT
        else:
          bankroll_alternating -= BET_AMOUNT

    else:
      if outcome == 0:
        zero_hits += 1
      else:
        double_hits += 1


    if outcome >= 1 and outcome <= 36:  # Exclude 0 and 00
        number_hits[outcome] += 1
        if outcome > 18:
            high_hits += 1
        else:
            low_hits += 1
        if outcome % 2 == 0:
            even_hits += 1
        else:
            odd_hits += 1

    # Update bankroll trackers after each spin
    bankroll_red_tracker.append(bankroll_red)
    bankroll_black_tracker.append(bankroll_black)
    bankroll_alternating_tracker.append(bankroll_alternating)

    # Alternate the color for next spin
    alternating_color = 'black' if alternating_color == 'red' else 'red'

print("# of red hits:", red_hits)
print("# of black hits:", black_hits)
print("# of 0 hits:", zero_hits)
print("# of 00 hits:", double_hits)
print("\n")
print("# of high hits:", high_hits)
print("# of low hits:", low_hits)
print("\n")
print("Final red bankroll:", bankroll_red)
print("Final black bankroll:", bankroll_black)
print("Final alternating bankroll:", bankroll_alternating)





# Graphs
plt.figure(figsize=(15, 10))

# First Graph: Red vs Black hits
plt.subplot(3, 2, 1)
plt.bar(["Red", "Black"], [red_hits, black_hits], color=['red', 'black'])
plt.title("Red vs Black Hits")

# Second Graph: High vs Low hits
plt.subplot(3, 2, 2)
plt.bar(["High (19-36)", "Low (1-18)"], [high_hits, low_hits])
plt.title("High vs Low Hits")

# Third Graph: Even vs Odd hits
plt.subplot(3, 2, 3)
plt.bar(["Even", "Odd"], [even_hits, odd_hits])
plt.title("Even vs Odd Hits")

# Fourth Graph: Hits per Number
plt.subplot(3, 2, 4)
plt.bar(number_hits.keys(), number_hits.values())
plt.title("Hits per Number")
plt.xticks(range(0, 37, 3))

# Fifth Graph: Bankroll Over Time
plt.subplot(3, 2, 5)
plt.plot(range(NUM_SPINS + 1), bankroll_red_tracker, label='Bet Red')
plt.plot(range(NUM_SPINS + 1), bankroll_black_tracker, label='Bet Black')
plt.plot(range(NUM_SPINS + 1), bankroll_alternating_tracker, label='Alternate Red/Black')
plt.title("Bankroll Over Time")
plt.xlabel('Number of Spins')
plt.ylabel('Bankroll')
plt.legend()

plt.tight_layout()
plt.show()
