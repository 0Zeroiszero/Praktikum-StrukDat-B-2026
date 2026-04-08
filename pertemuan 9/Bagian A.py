class Node:
    """Node Double Linked List yang menyimpan data buku."""
    __slots__ = ('judul', 'pengarang', 'prev', 'next')

    def __init__(self, judul: str, pengarang: str):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None


class DoubleLinkedList:
    """Double Linked List untuk mengelola daftar buku."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def insert_tail(self, judul: str, pengarang: str) -> None:
        """Menambahkan buku di akhir list. Kompleksitas: O(1)."""
        new_node = Node(judul, pengarang)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def delete_by_judul(self, judul: str) -> bool:
        """
        Menghapus node pertama dengan judul yang cocok.

        Returns:
            bool: True jika berhasil dihapus, False jika tidak ditemukan.
            Kompleksitas: O(n).
        """
        curr = self.head
        while curr:
            if curr.judul == judul:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev

                curr.prev = curr.next = None
                self._size -= 1
                return True
            curr = curr.next
        return False

    def print_forward(self) -> None:
        """Mencetak daftar buku dari head ke tail. Kompleksitas: O(n)."""
        print("[ Maju (Head → Tail) ]")
        if not self.head:
            print("  (List kosong)")
            return
        curr = self.head
        idx = 1
        while curr:
            print(f"  {idx}. \"{curr.judul}\" — {curr.pengarang}")
            curr = curr.next
            idx += 1

    def print_backward(self) -> None:
        """Mencetak daftar buku dari tail ke head. Kompleksitas: O(n)."""
        print("[ Mundur (Tail → Head) ]")
        if not self.tail:
            print("  (List kosong)")
            return
        curr = self.tail
        idx = 1
        while curr:
            print(f"  {idx}. \"{curr.judul}\" — {curr.pengarang}")
            curr = curr.prev
            idx += 1


if __name__ == "__main__":
    dll = DoubleLinkedList()

    dll.insert_tail("Laskar Pelangi", "Andrea Hirata")
    dll.insert_tail("Bumi Manusia", "Pramoedya Ananta Toer")
    dll.insert_tail("Sang Pemimpi", "Andrea Hirata")

    dll.print_forward()
    print()
    dll.print_backward()
    print()

    deleted = dll.delete_by_judul("Bumi Manusia")
    print(f"Hapus \"Bumi Manusia\": {'Berhasil' if deleted else 'Gagal'}\n")

    dll.print_forward()
    print()
    dll.print_backward()