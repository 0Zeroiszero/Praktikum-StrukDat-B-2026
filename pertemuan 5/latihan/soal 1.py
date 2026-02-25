nilai_tugas = [70, 85, 90, 65, 80]

# menggunakan pencarian indeks
for i in range(len(nilai_tugas)):
    if nilai_tugas[i] == 65:
        nilai_tugas[i] = 75

# menambahkan nilai 95 ke dalam list mengurutkan
nilai_tugas.append(95)
nilai_tugas.sort(reverse=True)
print(nilai_tugas)

# total seluruh nilai
print(sum(nilai_tugas))

# jika ada 100 - "Ada nilai sempura", else "Tidak ada"
try:
    if nilai_tugas.index(100):
        print("Ada nilai sempurna")
except ValueError:
    print("Tidak ada")
