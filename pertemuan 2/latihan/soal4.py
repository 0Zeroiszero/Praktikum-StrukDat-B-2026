mahasiswa = {
    "A001": {
        "nama":"Budi",
        "prodi":"Informatika",
        "ipk": 3.45
    },
    "A002": {
        "nama":"Siti",
        "prodi":"Sistem Informasi",
        "ipk": 3.20
    },
    "A003": {
        "nama":"Andi",
        "prodi":"Informatika",
        "ipk": 3.75
    }
}

print("Daftar IPK Mahasiswa yang lebih dari 3.5: ")
ipk_diatas_35 = [mahasiswa[index]["ipk"] for index in mahasiswa if mahasiswa[index]["ipk"] > 3.5]
seluruh_ipk = [mahasiswa[index]["ipk"] for index in mahasiswa]

avg = sum(seluruh_ipk) / len(seluruh_ipk)
print(f"Rerata IPK mahasiswa: {avg}")

"""
Menambahkan data baru
"""

mahasiswa["A004"] = {
        "nama":"Ikan Pari",
        "prodi":"Informatika",
        "ipk": 3.75
}

print(f"Data mahasiswa baru: {mahasiswa['A004']["nama"]}")