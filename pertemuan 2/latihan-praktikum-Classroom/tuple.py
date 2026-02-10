# Membuat tuple baru
empty_tuple = ()
tuple_from_list = tuple([1, 2, 3, 4, 5])

# count() - Menghitung jumlah kemunculan value
sample_tuple = (1, 2, 2, 3, 2, 4, 2)
count_result = sample_tuple.count(2)  # Hasil: 4

# index() - Mencari index pertama value dengan parameter tambahan
index_result1 = sample_tuple.index(2)
index_result2 = sample_tuple.index(2, 2)
index_result3 = sample_tuple.index(2, 4, 7)              

print("Tuple methods demo dengan parameter tambahan:")
print(f"Tuple: {sample_tuple}")
print(f"count(2): {count_result}")
print(f"index(2): {index_result1}")
print(f"index(2, 2): {index_result2}")
print(f"index(2, 4, 7): {index_result3}")