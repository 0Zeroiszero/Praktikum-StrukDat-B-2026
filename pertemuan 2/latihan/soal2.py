mahasiswa = ("A001", "Budi", "Informatika")
print(f"Nama mahasiswa = {mahasiswa[1]}")
loop = [daftar for daftar in mahasiswa]
print(loop)

# Alasan tuple tidak dapat diubah?
# Tuple tidak dapat diubah dengan alasan menjaga integritas data tertentu yang seharusnya tidak dapat diubah
# demi mencegah human error
