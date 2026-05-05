from node_bst import BST


def main():
    buku = [
        (50, "Dasar Pemrograman"),
        (30, "Struktur Data"),
        (70, "Kecerdasan Buatan"),
        (20, "Matematika Diskrit"),
        (40, "Basis Data"),
        (60, "Jaringan Komputer"),
        (80, "Sistem Operasi"),
    ]

    print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
    print("=" * 50)

    katalog = BST()
    for id_b, jud in buku:
        katalog.insert(id_b, jud)

    print()

    katalog.traverse_inorder()
    print()

    for cid in [60, 100]:
        print(f"[SEARCH] Mencari ID {cid}...", end=" ")
        hasil = katalog.search(cid)
        if hasil:
            print(f"Ditemukan! Judul: {hasil.judul}")
        else:
            print("Data tidak ditemukan.")

    print()
    print(f"[STATISTIK] ID Terkecil: {katalog.get_min().id_buku}")
    print(f"[STATISTIK] ID Terbesar: {katalog.get_max().id_buku}")

    print(f"\n[INFO] Tinggi (Height) Tree: {katalog.height()}")

    print("=" * 50)
    print("Simulasi Selesai!")


if __name__ == "__main__":
    main()
