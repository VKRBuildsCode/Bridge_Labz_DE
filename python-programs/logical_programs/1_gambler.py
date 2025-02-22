from random import random

total_wins = 0
total_bets = 0
stake = int(input("Enter the initial stake: $"))
goal = int(input("Enter the goal amount: $"))
num_trials = int(input("Enter the number of trials: "))
for trial in range(num_trials):
    current_stake = stake
    bets_made = 0  # Reset bets_made for each trial
    while 0 < current_stake < goal:
        bets_made += 1
        total_bets += 1  # increment the total bet count with each bet made
        # Simulate a 50/50 chance of winning or losing $1
        if random.random < 0.5:  # Win the bet
            current_stake += 1
        else:  # Lose the bet
            current_stake -= 1

    if current_stake == goal:
        total_wins += 1

# Calculate win and loss percentages
win_percentage = (total_wins / num_trials) * 100
loss_percentage = 100 - win_percentage

print(f"Initial Stake: ${stake}")
print(f"Goal: ${goal}")
print(f"Number of Trials: {num_trials}")
print(f"Total Wins: {total_wins}")
print(f"Total Bets Made: {total_bets}")
print(f"Win Percentage: {win_percentage:.2f}%")
print(f"Loss Percentage: {loss_percentage:.2f}%")