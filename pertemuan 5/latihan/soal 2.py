kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]

for i, v in kumpulan_nilai:
    if v >= 75:
        print(f"Selamat {i}, Anda Lulus!")
    elif v < 75:
        print(f"Maaf {i}, Anda harus remidi.")
