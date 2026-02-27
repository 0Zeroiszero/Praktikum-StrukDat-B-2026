sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

# siswa hadir dua sesi
print(sesi_pagi & sesi_siang)

# siswa hadir tanpa duplikat
siswa_hadir_tanpa_duplikat = set(sesi_siang.union(sesi_pagi))
print(siswa_hadir_tanpa_duplikat)

# sesi hari ini
gabungan_kedua_set = sesi_siang.union(sesi_pagi)
print(gabungan_kedua_set)
