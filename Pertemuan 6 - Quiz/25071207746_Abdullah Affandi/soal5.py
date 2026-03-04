import soal1, soal2, soal3, soal4

katalog = [
    {"nama": "Belajar Python", "harga": 75000, "stok": 5},
    {"nama": "Struktur Data", "harga": 95000, "stok": 3},
    {"nama": "Algoritma Dasar", "harga": 60000, "stok": 8},
]


def backss():
    print("=== Py BookStore ===")

    print("""
Daftar Menu:
1. Tambah buku
2. Tampilkan Semua Buku
3. Beli Buku
4. Laporan Penjualan
5. Keluar
      """)


backss()
lokasi = int(input("Menu: "))
riwayat = []

while lokasi < 6 and lokasi != 5:
    if lokasi == 1:
        berapa = int(input("Mau nambah berapa buku: "))
        for i in range(berapa):
            nama = [str(input(f"Nama buku ke-{i + 1}: "))]
            harga = [float(input(f"Harga buku ke-{i + 1}: "))]
            stok = [int(input(f"Stok buku ke-{i + 1}: "))]
            print()

            katalog.append(soal1.tambah_buku(*nama, *harga, *stok))

        print("DONE")
    if lokasi == 2:
        print(katalog)
    if lokasi == 3:
        buks = input("Nama buku yang dicari: ")
        buks_beli = int(input("Beli berapa: "))
        soal3.proses_transaksi(katalog=katalog, nama_buku=buks, jumlah_beli=buks_beli)
        riwayat.append(f"Buku dibeli: {buks}")
    if lokasi == 4:
        print(riwayat)

    lokasi = 0
    lokasi = int(input("Menu: "))
