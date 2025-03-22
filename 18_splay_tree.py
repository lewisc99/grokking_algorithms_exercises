class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class SplayTree:
  def __init__(self):
    self.root = None

  def _right_rotate(self, x):
    y = x.left
    x.left = y.right
    y.right = x
    return y

  def _left_rotate(self, x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

  def _splay(self, root, key):
    if root is None or root.key == key:
      return root

    if key < root.key:
      if root.left is None:
        return root

      if key < root.left.key:
        root.left.left = self._splay(root.left.left, key)
        root = self._right_rotate(root)
      elif key > root.left.key:
        root.left.right = self._splay(root.left.right, key)
        if root.left.right is not None:
          root.left = self._left_rotate(root.left)

      return root if root.left is None else self._right_rotate(root)
    else:
      if root.right is None:
        return root

      if key > root.right.key:
        root.right.right = self._splay(root.right.right, key)
        root = self._left_rotate(root)
      elif key < root.right.key:
        root.right.left = self._splay(root.right.left, key)
        if root.right.left is not None:
          root.right = self._right_rotate(root.right)

      return root if root.right is None else self._left_rotate(root)

  def insert(self, key):
    if self.root is None:
      self.root = Node(key)
      return

    self.root = self._splay(self.root, key)

    if self.root.key == key:
      return

    new_node = Node(key)
    if key < self.root.key:
      new_node.right = self.root
      new_node.left = self.root.left
      self.root.left = None
    else:
      new_node.left = self.root
      new_node.right = self.root.right
      self.root.right = None

    self.root = new_node

  def search(self, key):
    self.root = self._splay(self.root, key)
    return self.root is not None and self.root.key == key

  def pre_order(self, node):
    if node is not None:
      print(node.key, end=" ")
      self.pre_order(node.left)
      self.pre_order(node.right)

# Example usage
if __name__ == "__main__":
  tree = SplayTree()
  keys = [10, 20, 30, 40, 50, 25]

  for key in keys:
    tree.insert(key)

  print("Pre-order traversal of the splay tree is:")
  tree.pre_order(tree.root)
  print()

  print("Searching for 25 in the splay tree:")
  found = tree.search(40)
  print("Found" if found else "Not Found")