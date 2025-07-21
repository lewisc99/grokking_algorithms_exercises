def knapsack_max_value(item_weights, item_values, capacity):
    """
    Solve the 0/1 Knapsack problem:
    Given lists of item_weights and item_values, and the knapsack capacity,
    return the maximum total value that fits without exceeding capacity.
    """
    # Number of items
    num_items = len(item_weights)

    # Create a DP table with dimensions (num_items + 1) x (capacity + 1)
    # dp_table[i][w] will hold the max value achievable using the first i items
    # with a weight limit of w.
    dp_table = [[0 for w in range(capacity + 1)] for i in range(num_items + 1)]

    # Build the table row by row
    for item_index in range(1, num_items + 1):
        current_weight = item_weights[item_index - 1]
        current_value = item_values[item_index - 1]

        for allowed_weight in range(capacity + 1):
            # Case 1: we don't take the current item
            value_without_item = dp_table[item_index - 1][allowed_weight]

            # Case 2: we take the current item (if it fits)
            if current_weight <= allowed_weight:
                value_with_item = (
                    current_value
                    + dp_table[item_index - 1][allowed_weight - current_weight]
                )
            else:
                value_with_item = 0  # can't take it if overweight

            # Choose the better of the two options
            dp_table[item_index][allowed_weight] = max(
                value_without_item, value_with_item
            )

    # The bottom-right cell is the answer: max value using all items and full capacity
    return dp_table[num_items][capacity]


# --- Example Usage ---
if __name__ == "__main__":
    # Suppose we have three items:
    #   Weights: [3, 4, 6]
    #   Values:  [2, 3, 1]
    # And our knapsack can carry at most 8 units of weight.
    weights = [3, 4, 6]
    values = [2, 3, 1]
    max_capacity = 8

    max_val = knapsack_max_value(weights, values, max_capacity)
    print(f"Maximum value in knapsack: {max_val}")
    # Expected output: 5
    # (Take items 1 and 2: weight 3+4=7, value 2+3=5)
