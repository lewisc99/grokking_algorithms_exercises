# Greedy Algorithm Example: Coin Change Problem

# Problem: You need to give change for a certain amount of money using the least number of coins.
# You have coins of different values. What is the minimum number of coins you need?

# Let's say we have coins of 25, 10, 5, and 1 cent.

def get_min_coins(amount):
  coins = [25, 10, 5, 1]  # Coin values, from largest to smallest
  result = []  # List to store the coins we use

  for coin in coins:
    while amount >= coin:
      amount -= coin
      result.append(coin)  # Add the coin to our result

  return result

# Example: Let's make change for 63 cents
change = get_min_coins(63)
print("Coins used:", change)
print("Number of coins:", len(change))