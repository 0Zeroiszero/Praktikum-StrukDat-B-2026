transaksi = [
    {"produk": "Buku", "harga": 10000, "jumlah": 3},
    {"produk": "Pena", "harga": 5000, "jumlah": 10},
    {"produk": "Penghapus", "harga": 2000, "jumlah": 2},
]

# mengubah jumlah menjadi 8
for isi in transaksi:
    if isi.get("produk") == "Buku":
        isi.update({"jumlah": 8})

# menambahkan dua data baru
transaksi.append({"produk": "Buku_adwawdaw", "harga": 10456500, "jumlah": 100})
transaksi.append({"produk": "lapangan", "harga": 2210456500, "jumlah": 100})

# print sesuai format Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.
sesuai_format = []
for isi in transaksi:
    sesuai_format.append(
        f"Produk: {isi.get('produk')} | Total: {isi.get('harga') * isi.get('jumlah')}"
    )

print(*sesuai_format)
