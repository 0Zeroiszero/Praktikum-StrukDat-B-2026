class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class AntreanLinkedList:
    def __init__(self):
        self.head = None

    def append(self, nama_pasien):
        new_node = Node(nama_pasien)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def tampilkan_antrean(self):
        if not self.head:
            print("Antrean kosong")
            return
        current = self.head
        hasil = []
        while current:
            hasil.append(current.data)
            current = current.next
        print(" -> ".join(hasil))


def insert_at_position(head, nama_pasien, posisi):
    new_node = Node(nama_pasien)
    
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    
    if posisi > count + 1:
        print(f"Posisi {posisi} melebihi jumlah pasien ({count}). Pasien ditambahkan di akhir.")
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head
    
    if posisi == 1:
        new_node.next = head
        print(f"Pasien '{nama_pasien}' disisipkan pada posisi {posisi}")
        return new_node
    
    current = head
    for _ in range(posisi - 2):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    print(f"Pasien '{nama_pasien}' disisipkan pada posisi {posisi}")
    
    return head

antrean_rs = AntreanLinkedList()

data_awal = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]
for pasien in data_awal:
    antrean_rs.append(pasien)

print("=== Antrean Awal ===")
antrean_rs.tampilkan_antrean()
print()

antrean_rs.head = insert_at_position(antrean_rs.head, "Pasien D (Darurat)", 2)

print("=== Setelah Sisip Posisi 2 ===")
antrean_rs.tampilkan_antrean()
print()

antrean_rs.head = insert_at_position(antrean_rs.head, "Pasien E (Baru)", 10)

print("=== Setelah Coba Posisi 10 ===")
antrean_rs.tampilkan_antrean()