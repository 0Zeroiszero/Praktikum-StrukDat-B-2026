from .node import Node

class QueueLinkedList:
    """
    Queue menggunakan si Node untuk pasien
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        self._nomor_urut = 0

    def isempty(self):
        """Cek antrian kosong"""
        return self._size == 0

    def enqueue(self, nama, keluhan):
        """Menambahkan pasien baru ke antrian paling belakang"""
        new_node = Node(nama, keluhan)
        self._nomor_urut += 1

        if self.isempty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
        print(
            f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._nomor_urut})"
        )

    def dequeue(self):
        """Panggil pasien dan keluarkan dari antrian"""
        if self.isempty():
            # Kalau kosong skip aja bosku
            print("[PANGGIL] Antrian kosong, tidak ada pasien yang bisa dipanggil.")
            return None

        removed_node = self.head
        self.head = self.head.next
        self._size -= 1

        if self.head is None:
            self.tail = None

        print(
            f"[PANGGIL] Dokter memanggil: {removed_node.nama} (keluhan: {removed_node.keluhan})"
        )
        return removed_node

    def peek(self):
        """Melihat pasien paling depan tanpa mengeluarkannya"""
        if self.isempty():
            # Kalau depan kosong tinggal bilang kosong
            print("[PEEK] Antrian kosong.")
            return None

        print(f"[PEEK] Pasien berikutnya: {self.head.nama} - {self.head.keluhan}")
        return

    def size(self):
        """Mengembalikan jumlah pasien dalam antrian"""
        return self._size

    def clear(self):
        """Mengosongkan seluruh antrian"""
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def display(self):
        """Menampilkan seluruh antrian saat ini"""
        if self.isempty():
            print("[ANTRIAN SAAT INI] Antrian kosong.")
            return

        print("[ANTRIAN SAAT INI]")
        current = self.head
        idx = 1
        while current:
            print(f"{idx}. {current.nama:<8} -> {current.keluhan}")
            current = current.next
            idx += 1