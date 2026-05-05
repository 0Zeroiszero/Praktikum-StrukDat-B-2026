class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.new = Node(data)
        if self.root is None:
            self.root = self.new
            return

        self.P = self.root
        self.Q = self.root

        while self.Q is not None:
            self.P = self.Q
            if self.new.data < self.P.data:
                self.Q = self.P.left
            elif self.new.data > self.P.data:
                self.Q = self.P.right
            else:
                print("Data sudah ada, tidak bisa ditambahkan")
                return

        if self.new.data < self.P.data:
            self.P.left = self.new
        else:
            self.P.right = self.new

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)


pertama = BinarySearchTree()
pertama.insert(10)
pertama.insert(5)
pertama.insert(15)
pertama.insert(3)

pertama.inorder(pertama.root)