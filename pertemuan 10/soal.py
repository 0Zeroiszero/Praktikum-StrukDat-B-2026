# BAGIAN 1
class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python
    
    def is_empty(self):
        # Tulis kode di sini
        return self.size == 0
    
    def push(self, url):
        # Tulis kode di sini (Petunjuk: gunakan append)
        self.items.append(url)

    def pop(self):
        # Tulis kode di sini (Petunjuk: pastikan tidak kosong, lalu gunakan pop)
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Riwayat kosong"
    
    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan elemen indeks terakhir [-1])
        return self.items[-1]

    def size(self):
        # Tulis kode di sini (Petunjuk: gunakan len())
        return len(self.items)
    
web = StackList()
web.push("Halo")
print(web.peek())
print(web.size())
print(web.pop())

# BAGIAN 2

class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran

    def is_empty(self):
        return self.top is None

    def push(self, url):
    # Tulis kode di sini
    # 1. Buat Node baru
    # 2. Hubungkan 'next' node baru ke 'top' saat ini
    # 3. Jadikan node baru sebagai 'top' yang baru
    # 4. Tambahkan nilai 'count'
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
    # Tulis kode di sini
    # 1. Periksa is_empty()
    # 2. Simpan url dari 'top' saat ini
    # 3. Geser 'top' ke node berikutnya (top = top.next)
    # 4. Kurangi nilai 'count'
    # 5. Kembalikan url yang disimpan
        if self.is_empty():
            return "Stack is empty"
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url

    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan nilai url dari 'top')
        if self.is_empty():
            return "Stack is empty"
        return self.top.url

    def size(self):
        # Tulis kode di sini (Petunjuk: kembalikan nilai variabel 'count')
        return self.count
    
list = StackLinkedList()
list.push("https://kopi.com")
print(list.peek())
list.push("https://url.com")
print(list.peek())
print(list.size())

print(list.pop())
print(list.pop())
print(list.size())
