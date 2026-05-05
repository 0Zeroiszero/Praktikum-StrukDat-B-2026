class Node:
    """Representasi satu node dalam Binary Tree"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Implementasi Binary Tree"""

    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node, data):
        """Memasukkan child kiri dari suatu node"""
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        """Memasukkan child kanan dari suatu node"""
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

    def inorder(self, node):
        if node is None:
            return ""
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)


# Membuat instance tree
tree = BinaryTree()

# Membuat struktur tree:
#       F
#      /  \
#     B    G
#    / \    \
#   A   D    I
#      / \   /
#     C   E  H

tree.insert_root("F")
# Kanankan
tree.insert_right(tree.root, "G")
tree.insert_right(tree.root.right, "I")
tree.insert_left(tree.root.right.right, "H")

# Kirikan
tree.insert_left(tree.root, "B")
tree.insert_left(tree.root.left, "A")
tree.insert_right(tree.root.left, "D")
tree.insert_right(tree.root.left.right, "E")
tree.insert_left(tree.root.left.right, "C") 

tree.inorder(tree.root)