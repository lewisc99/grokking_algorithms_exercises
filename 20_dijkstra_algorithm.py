import math

# Create a graph as a dictionary
graph = {}
graph["you"] = ["alice", "bob", "claire"]  # Example unrelated graph for demonstration

# Initialize the graph with nodes and their neighbors
graph["start"] = {}
graph["start"]["a"] = 6  # Cost to reach "a" from "start" is 6
graph["start"]["b"] = 2  # Cost to reach "b" from "start" is 2

# Print the neighbors of "start"
print(list(graph["start"].keys()))  # Output: ['a', 'b']
print((graph["start"]["a"]))        # Output: 6
print((graph["start"]["b"]))        # Output: 2

# Add neighbors for "a" and "b"
graph["a"] = {}
graph["a"]["fin"] = 1  # Cost to reach "fin" from "a" is 1

graph["b"] = {}
graph["b"]["a"] = 3    # Cost to reach "a" from "b" is 3
graph["b"]["fin"] = 5  # Cost to reach "fin" from "b" is 5

graph["fin"] = {}  # "fin" has no neighbors

# Define infinity for unreachable nodes
infinity = math.inf

# Initialize costs table
costs = {}
costs["a"] = 6       # Initial cost to reach "a" is 6
costs["b"] = 2       # Initial cost to reach "b" is 2
costs["fin"] = infinity  # Initial cost to reach "fin" is infinity (unknown)

# Initialize parents table
parents = {}
parents["a"] = "start"  # "a" is reached from "start"
parents["b"] = "start"  # "b" is reached from "start"
parents["fin"] = None   # "fin" has no parent yet

# Keep track of processed nodes
processed = set()

# Function to find the lowest-cost node that hasn't been processed
def find_lowest_cost_node(costs, processed):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Main algorithm loop
node = find_lowest_cost_node(costs, processed)  # Find the lowest-cost node
while node is not None:  # Continue until all nodes are processed
    cost = costs[node]  # Current cost to reach this node
    neighbors = graph[node]  # Get neighbors of the current node
    for n in neighbors.keys():  # Iterate through each neighbor
        new_cost = cost + neighbors[n]  # Calculate the new cost to reach the neighbor
        if costs[n] > new_cost:  # If the new cost is lower than the current cost
            costs[n] = new_cost  # Update the cost to reach the neighbor
            parents[n] = node    # Update the parent of the neighbor
    processed.add(node)  # Mark the node as processed
    node = find_lowest_cost_node(costs, processed)  # Find the next lowest-cost node

# Print the results
print("Lowest cost to each node:")
for node in costs:
    print(node, ":", costs[node])  # Output the cost to reach each node

print("lowest cost to fin:", costs["fin"])  # Output the cost to reach "fin"