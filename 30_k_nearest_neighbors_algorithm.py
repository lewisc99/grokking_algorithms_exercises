import math
from collections import Counter

# Data: [size, redness, type]
fruits = [
    {"id": 1, "features": [8, 9], "type": "grapefruit"},
    {"id": 2, "features": [7, 8], "type": "grapefruit"},
    {"id": 3, "features": [9, 7], "type": "grapefruit"},
    {"id": 4, "features": [3, 4], "type": "orange"},
    {"id": 5, "features": [4, 3], "type": "orange"},
    {"id": 6, "features": [2, 5], "type": "orange"},
]
new_fruit = {"id": 0, "features": [6, 6]}
k = 3


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# 1. Calculate distances
distances = []
for fruit in fruits:
    dist = euclidean_distance(new_fruit["features"], fruit["features"])
    distances.append({"id": fruit["id"], "type": fruit["type"], "distance": dist})

# 2. Sort distances
distances.sort(key=lambda x: x["distance"])

# 3. Get k-nearest neighbors
neighbors = distances[:k]

# 4. Get the vote from neighbors
neighbor_types = [neighbor["type"] for neighbor in neighbors]
most_common = Counter(neighbor_types).most_common(1)[0][0]

print(f"Classification: {most_common}")
