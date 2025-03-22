class BTreeNode:
  def __init__(self, t, leaf=False):
    self.t = t  # Minimum degree (defines the range for number of keys)
    self.leaf = leaf  # True if leaf node, else False
    self.keys = []  # List of keys
    self.children = []  # List of child pointers

  def insert_non_full(self, key):
    i = len(self.keys) - 1
    if self.leaf:
      self.keys.append(None)
      while i >= 0 and key < self.keys[i]:
        self.keys[i + 1] = self.keys[i]
        i -= 1
      self.keys[i + 1] = key
    else:
      while i >= 0 and key < self.keys[i]:
        i -= 1
      i += 1
      if len(self.children[i].keys) == 2 * self.t - 1:
        self.split_child(i)
        if key > self.keys[i]:
          i += 1
      self.children[i].insert_non_full(key)

  def split_child(self, i):
    t = self.t
    y = self.children[i]
    z = BTreeNode(t, y.leaf)
    self.children.insert(i + 1, z)
    self.keys.insert(i, y.keys[t - 1])
    z.keys = y.keys[t:(2 * t - 1)]
    y.keys = y.keys[0:(t - 1)]
    if not y.leaf:
      z.children = y.children[t:(2 * t)]
      y.children = y.children[0:t]

  def traverse(self):
    for i in range(len(self.keys)):
      if not self.leaf:
        self.children[i].traverse()
      print(self.keys[i], end=' ')
    if not self.leaf:
      self.children[len(self.keys)].traverse()

  def search(self, key):
    i = 0
    while i < len(self.keys) and key > self.keys[i]:
      i += 1
    if i < len(self.keys) and key == self.keys[i]:
      return self
    if self.leaf:
      return None
    return self.children[i].search(key)


class BTree:
  def __init__(self, t):
    self.root = BTreeNode(t, True)
    self.t = t

  def insert(self, key):
    root = self.root
    if len(root.keys) == 2 * self.t - 1:
      temp = BTreeNode(self.t, False)
      temp.children.insert(0, root)
      temp.split_child(0)
      i = 0
      if temp.keys[0] < key:
        i += 1
      temp.children[i].insert_non_full(key)
      self.root = temp
    else:
      root.insert_non_full(key)

  def traverse(self):
    if self.root:
      self.root.traverse()

  def search(self, key):
    if self.root:
      return self.root.search(key)
    return None


# Example usage
if __name__ == "__main__":
  btree = BTree(3)
  keys = [10, 20, 5, 6, 12, 30, 7, 17]
  for key in keys:
    btree.insert(key)

  print("Traversal of the constructed B-Tree is:")
  btree.traverse()

  key = 6
  if btree.search(key):
    print(f"\nKey {key} is present in the B-Tree")
  else:
    print(f"\nKey {key} is not present in the B-Tree")