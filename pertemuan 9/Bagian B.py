class Node:
    """Node Circular Linked List yang menyimpan nama pelanggan."""

    __slots__ = ("nama", "next")

    def __init__(self, nama: str):
        self.nama = nama
        self.next = None


class CircularQueue:
    """Circular Linked List untuk mengelola antrian kasir."""

    def __init__(self):
        self.tail = None

    def insert_tail(self, nama: str) -> None:
        """Menambahkan pelanggan di akhir antrian. Kompleksitas: O(1)."""
        new_node = Node(nama)
        if not self.tail:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def delete_head(self) -> bool:
        """
        Menghapus pelanggan di awal antrian (sudah dilayani).

        Returns:
            bool: True jika berhasil dihapus, False jika antrian kosong.
            Kompleksitas: O(1).
        """
        if not self.tail:
            return False

        head = self.tail.next
        if head == self.tail:
            self.tail = None
        else:
            self.tail.next = head.next

        head.next = None
        return True

    def print_antrian(self) -> None:
        """Mencetak satu putaran penuh antrian. Kompleksitas: O(n)."""
        if not self.tail:
            print("  (Antrian kosong)")
            return

        print("[ Antrian Kasir ]")
        curr = self.tail.next
        while True:
            print(f"  - {curr.nama}")
            curr = curr.next
            if curr == self.tail.next:
                break


if __name__ == "__main__":
    cq = CircularQueue()

    cq.insert_tail("Andi")
    cq.insert_tail("Budi")
    cq.insert_tail("Citra")
    cq.insert_tail("Dina")
    cq.print_antrian()
    print()

    cq.insert_tail("Edo")
    cq.print_antrian()
    print()

    deleted = cq.delete_head()
    print(f'Hapus "Andi": {"Berhasil" if deleted else "Gagal"}')
    cq.print_antrian()
