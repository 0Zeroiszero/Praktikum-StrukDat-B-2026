class Node:
    """Simpul pohon biner dengan pointer anak kiri dan kanan."""
    def __init__(self, data):
        self.data = data
        self.left = None    # pointer anak kiri
        self.right = None   # pointer anak kanan


class BinaryTree:
    """Pohon biner manual dengan tiga metode traversal dan pencarian leaf."""
    def __init__(self):
        self.root = None

    # Insert Manual - Bangun struktur sesuai skenario
    def insert_manual(self):
        """Membangun pohon A-B-C-D-E-F."""
        print("[INFO] Membangun Struktur Gudang...")
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        self.root.right.right = Node('F')
        print("[INFO] Struktur berhasil dibuat.\n")

    # Pre-Order - Rekursif
    def traverse_preorder(self):
        """Kunjungan pre-order (root, kiri, kanan)."""
        hasil = []
        def _pre(node):
            if node:
                hasil.append(node.data)
                _pre(node.left)
                _pre(node.right)
        _pre(self.root)
        return hasil

    # In-Order - Rekursif
    def traverse_inorder(self):
        """Kunjungan in-order (kiri, root, kanan)."""
        hasil = []
        def _in(node):
            if node:
                _in(node.left)
                hasil.append(node.data)
                _in(node.right)
        _in(self.root)
        return hasil

    # Post-Order - Rekursif
    def traverse_postorder(self):
        """Kunjungan post-order (kiri, kanan, root)."""
        hasil = []
        def _post(node):
            if node:
                _post(node.left)
                _post(node.right)
                hasil.append(node.data)
        _post(self.root)
        return hasil

    # Leaf Nodes - Rekursif
    def get_leaf_nodes(self):
        """Kumpulkan semua node yang tidak memiliki anak."""
        daun = []
        def _leaf(node):
            if node:
                if node.left is None and node.right is None:
                    daun.append(node.data)
                _leaf(node.left)
                _leaf(node.right)
        _leaf(self.root)
        return daun