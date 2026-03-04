import soal2


def proses_transaksi(katalog, nama_buku, jumlah_beli):
    hasil_cari = soal2.cari_buku(katalog=katalog, keyword=nama_buku)
    # katalog[i]['nama']

    if katalog[hasil_cari]["stok"] <= 0:
        print("Peringatan stok tidak cukup")
        return

    if hasil_cari and katalog[hasil_cari]["stok"]:
        bayar = jumlah_beli * katalog[hasil_cari]["harga"]
        katalog[hasil_cari]["stok"] -= jumlah_beli
        print(f"Total bayar: {bayar}")
        return bayar
