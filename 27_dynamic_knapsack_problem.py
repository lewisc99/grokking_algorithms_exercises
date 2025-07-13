# Define a class to represent an item
class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


# Define the items (same as the HTML example)
items = [Item("Guitar", 1, 1500), Item("Stereo", 4, 3000), Item("Laptop", 3, 2000)]

# Define the maximum weight of the knapsack
max_weight = 4

# Initialize a DP table:
# dp[i][w] will hold the maximum value we can get by considering the first (i+1) items and a knapsack of capacity w
# Let's break this down for clarity:

# Number of items
n = len(items)

# Create a table with n rows (one for each item) and (max_weight + 1) columns (for each possible weight)
dp = []
for i in range(n):
  row = []
  for w in range(max_weight + 1):
    row.append(0)  # Start with 0 value for each cell
  dp.append(row)

# Track the items included in the optimal solution
# This creates a table (list of lists) where each cell holds a list of item names.
# selected_items[i][w] will store the list of item names chosen for the first (i+1) items and weight w.
selected_items = []
for i in range(n):
  row = []
  for w in range(max_weight + 1):
    row.append([])  # Start with an empty list for each cell
  selected_items.append(row)

# Fill the DP table
for i in range(len(items)):
    for w in range(1, max_weight + 1):
        item = items[i]

        # Option 1: exclude the item (take the value from the row above)
        exclude_value = dp[i - 1][w] if i > 0 else 0
        exclude_items = selected_items[i - 1][w] if i > 0 else []

        # Option 2: include the item if it fits
        if item.weight <= w:
            remaining_weight = w - item.weight
            include_value = item.value
            include_items = [item.name]

            if i > 0 and remaining_weight > 0:
                include_value += dp[i - 1][remaining_weight]
                include_items += selected_items[i - 1][remaining_weight]

            # Choose better of the two options
            if include_value > exclude_value:
                dp[i][w] = include_value
                selected_items[i][w] = include_items
            else:
                dp[i][w] = exclude_value
                selected_items[i][w] = exclude_items
        else:
            # Can't include item; only option is to exclude
            dp[i][w] = exclude_value
            selected_items[i][w] = exclude_items

# Result: bottom-right cell of the table
max_value = dp[-1][-1]
items_taken = selected_items[-1][-1]

# Print result
print("Maximum value:", f"${max_value}")
print("Items to take:", ", ".join(items_taken))
