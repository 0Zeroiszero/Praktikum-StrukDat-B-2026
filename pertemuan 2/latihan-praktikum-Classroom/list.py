# Membuat list baru
my_list = []

# append() - Menambahkan elemen di akhir list
my_list.append(1)
my_list.append(2)

# extend() - Menambahkan semua elemen dari iterable
my_list.extend([3, 4])

# insert() - Menyisipkan elemen pada indeks tertentu
my_list.insert(1, 'baru')

# remove() - Menghapus elemen pertama dengan nilai tertentu
my_list.remove('baru')

# pop() - Menghapus dan mengembalikan elemen (indeks tertentu atau terakhir)
last_item = my_list.pop()
first_item = my_list.pop(0)

# clear() - Menghapus semua elemen
temp_list = [1, 2, 3]
temp_list.clear()

# index() - Mengembalikan indeks dari elemen dengan nilai tertentu
search_list = [10, 20, 30, 20, 40]
idx = search_list.index(20)
idx2 = search_list.index(20, 2)

# count() - Menghitung jumlah kemunculan elemen
count_val = search_list.count(20)

# sort() - Mengurutkan elemen
sort_list = [5, 2, 8, 1]
sort_list.sort()
sort_list.sort(reverse=True)

# reverse() - Membalik urutan elemen
reverse_list = [1, 2, 3, 4]
reverse_list.reverse()

# copy() - Mengembalikan salinan dari list
original = [1, 2, 3]
duplicate = original.copy()

# Menampilkan hasil
print("Hasil implementasi method list:")
print(f"Setelah append dan extend: {[1, 2, 3, 4]}")
print(f"Nilai yang dipop: last={last_item}, first={first_item}")
print(f"Index dari 20: {idx}, Index 20 dari posisi 2: {idx2}")
print(f"Jumlah kemunculan 20: {count_val}")
print(f"List setelah reverse: {reverse_list}")
print(f"Salinan list: {duplicate}")