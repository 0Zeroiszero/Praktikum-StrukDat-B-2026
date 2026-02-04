kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

print(f'Mata kuliah oleh kedua kelas: {kelas_A | kelas_B}')
print(f'Mata kuliah hanya diambil kelas A: {kelas_A}')
print(f'Seluruh mata kuliah unik: {kelas_A ^ kelas_B}')