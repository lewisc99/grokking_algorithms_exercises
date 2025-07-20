# Define a class to represent an item
class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


def knapsack_recursive(items, max_weight, idx=0):
    # Base case: no items left or no capacity
    if idx == len(items) or max_weight == 0:
        return 0, []

    item = items[idx]
    # Option 1: skip the item
    value_excl, items_excl = knapsack_recursive(items, max_weight, idx + 1)

    # Option 2: include the item (if it fits)
    if item.weight <= max_weight:
        value_incl, items_incl = knapsack_recursive(
            items, max_weight - item.weight, idx + 1
        )
        value_incl += item.value
        items_incl = [item.name] + items_incl

        # Choose better option
        if value_incl > value_excl:
            return value_incl, items_incl

    return value_excl, items_excl


# Define the items (same as the HTML example)
items = [Item("Guitar", 1, 1500), Item("Stereo", 4, 3000), Item("Laptop", 3, 2000)]
max_weight = 4

max_value, items_taken = knapsack_recursive(items, max_weight)
print("Maximum value:", f"${max_value}")
print("Items to take:", ", ".join(items_taken))