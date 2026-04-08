antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

print("Data Awal (Antrean saat ini):", antrean_array)
print()


def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    """
    Menyisipkan pasien darurat ke dalam antrean pada posisi tertentu.
    
    Analisis:
    Ketika pasien baru disisipkan di tengah antrean menggunakan .insert(),
    semua pasien yang berada di belakang posisi penyisipan akan bergeser
    ke indeks yang lebih tinggi (mundur satu posisi).
    """
    antrean_array.insert(posisi - 1, nama_pasien)
    print(f"Pasien '{nama_pasien}' disisipkan pada posisi {posisi}")

sisipkan_pasien_darurat_array("Pasien D (DARURAT)", 2)

print()
print("Antrean Akhir:", antrean_array)