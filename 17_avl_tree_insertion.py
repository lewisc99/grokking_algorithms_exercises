class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initial height
 
class AVLTree:
    # Get height of a node
    def height(self, node):
        return node.height if node else 0
 
    # Get balance factor
    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0
 
    # Right rotate (LL Case)
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        return x
 
    # Left rotate (RR Case)
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        return y
 
    # Insert into AVL tree
    def insert(self, root, key):
        # 1. Perform standard BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        # 2. Update height
        root.height = max(self.height(root.left), self.height(root.right)) + 1
 
        # 3. Get balance factor
        balance = self.get_balance(root)
 
        # 4. Perform rotations if needed
        if balance > 1 and key < root.left.key:  # LL Case
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:  # RR Case
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:  # LR Case
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:  # RL Case
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
 
        return root  # Return unchanged root
 
# Example usage
avl = AVLTree()
root = None
for key in [10, 20, 30, 40, 50, 25]:
  root = avl.insert(root, key)
print("AVL Tree created successfully!")

# Function to print the AVL tree in a structured manner
def print_tree(node, level=0, prefix="Root: "):
  if not node:
    return
  print(" " * (level * 4) + prefix + str(node.key))
  if node.left:
    print_tree(node.left, level + 1, "L--- ")
  if node.right:
    print_tree(node.right, level + 1, "R--- ")

# Print the AVL tree
print("Illustration of the AVL tree:")
print_tree(root)