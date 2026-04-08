class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HistoryLinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def tambah_pencarian_linked(self, keyword):
        new_node = Node(keyword)
        new_node.next = self.head
        self.head = new_node

    def tampilkan_history(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("null")

history = HistoryLinkedList("google.com")
history.tambah_pencarian_linked("python.org")

history.tampilkan_history()
history.tambah_pencarian_linked("huggingface.com")
history.tampilkan_history()