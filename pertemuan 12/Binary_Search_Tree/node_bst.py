class Node:
    """Simpul penyimpan data buku (ID, judul) dan pointer anak."""

    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None  # pointer anak kiri
        self.right = None  # pointer anak kanan


class BST:
    """Binary Search Tree manual tanpa struktur data bawaan Python."""

    def __init__(self):
        self.root = None  # pointer akar

    # Insert - Rekursif
    def insert(self, id_buku, judul):
        """Tambah buku ke BST sesuai aturan kiri < induk < kanan."""
        if self.root is None:
            self.root = Node(id_buku, judul)
            print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
            return

        def _insert(current, id_buku, judul):
            if id_buku < current.id_buku:
                if current.left is None:
                    current.left = Node(id_buku, judul)
                    print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
                else:
                    _insert(current.left, id_buku, judul)
            elif id_buku > current.id_buku:
                if current.right is None:
                    current.right = Node(id_buku, judul)
                    print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")
                else:
                    _insert(current.right, id_buku, judul)
            else:
                print(f"[INSERT] ID {id_buku} sudah ada, data diabaikan.")

        _insert(self.root, id_buku, judul)

    # Search - Iteratif
    def search(self, id_buku):
        """Cari buku berdasarkan ID. Kembalikan Node jika ditemukan, selain itu None."""
        current = self.root
        while current is not None:
            if id_buku == current.id_buku:
                return current
            elif id_buku < current.id_buku:
                current = current.left
            else:
                current = current.right
        return None

    # Traverse In-Order - Rekursif + Counter Int
    def traverse_inorder(self):
        """Tampilkan seluruh buku terurut ID (kiri–akar–kanan)."""
        print("[INFO] Koleksi Buku (In-Order Traversal):")
        if self.root is None:
            print("  (Kosong)")
            return

        def _inorder(node, counter):
            if node is not None:
                counter = _inorder(node.left, counter)
                print(f"{counter}. {node.id_buku} - {node.judul}")
                counter += 1
                counter = _inorder(node.right, counter)
            return counter

        _inorder(self.root, 1)

    # Get Min - Iteratif Pointer Kiri
    def get_min(self):
        """Kembalikan node dengan ID terkecil."""
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    # Get Max - Iteratif Pointer Kanan
    def get_max(self):
        """Kembalikan node dengan ID terbesar."""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    # Height - Rekursif
    def height(self):
        """Hitung tinggi pohon (jumlah edge)."""

        def _height(node):
            if node is None:
                return -1
            left_h = _height(node.left)
            right_h = _height(node.right)
            return 1 + max(left_h, right_h)

        return _height(self.root)
