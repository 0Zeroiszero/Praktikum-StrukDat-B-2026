# Membuat set baru
empty_set = set()
set_from_iterable = set([1, 2, 3, 2, 1])  # Hasil: {1, 2, 3}

# add() - Menambah elemen ke set
my_set = {1, 2, 3}
my_set.add(4)

# clear() - Menghapus semua elemen
temp_set = {1, 2, 3}
temp_set.clear()

# copy() - Membuat shallow copy
original_set = {1, 2, 3}
copied_set = original_set.copy()

# discard() - Menghapus elemen (tidak error jika tidak ada)
discard_set = {1, 2, 3}
discard_set.discard(2)  # Hapus elemen 2
discard_set.discard(99)  # Tidak error walaupun 99 tidak ada

# pop() - Menghapus dan mengembalikan elemen acak
pop_set = {1, 2, 3, 4}
popped = pop_set.pop()  # Menghapus elemen acak

# remove() - Menghapus elemen (error jika tidak ada)
remove_set = {1, 2, 3}
remove_set.remove(2)  # Hapus elemen 2
# remove_set.remove(99)  # Ini akan menyebabkan KeyError

# Menampilkan hasil
print("Hasil implementasi method set:")
print(f"Set dari iterable: {set_from_iterable}")
print(f"Set setelah add(4): {my_set}")
print(f"Set setelah discard(2) dan discard(99): {discard_set}")
print(f"Elemen yang dipop: {popped}, set sisanya: {pop_set}")
print(f"Set setelah remove(2): {remove_set}")
print(f"Salinan set: {copied_set}")