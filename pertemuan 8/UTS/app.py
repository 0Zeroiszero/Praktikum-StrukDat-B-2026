from tabulate import tabulate

# data studi kasus pasien

pasien_hari_ini = [
 {"id": "P001", "nama": "Andi", "usia": 34, "penyakit":
"Flu", "bayar": False},
 {"id": "P002", "nama": "Budi", "usia": 22, "penyakit":
"Tifus", "bayar": True},
 {"id": "P003", "nama": "Cici", "usia": 45, "penyakit":
"Flu", "bayar": False},
 {"id": "P004", "nama": "Dani", "usia": 30, "penyakit":
"Maag", "bayar": True},
 {"id": "P005", "nama": "Eva", "usia": 28, "penyakit":
"Tifus", "bayar": False},
 {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit":
"Maag", "bayar": False},
 {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit":
"Maag", "bayar": False, 'prioritas':'Darurat'},
]

# ======
# SOAL 1
# ======
def tampilkan_pasien() -> str:
    """tampilkan pasien"""
    tl = pasien_hari_ini.copy()

    for i in tl:
        if i['bayar']:
            i['bayar'] = "Lunas"
        else:
            i['bayar'] = "Belum bayar"

    t = tabulate(tl, tablefmt="pipe")

    return t

# Penampilan data klinik
print("===== DATA PASIEN KLINIK =====")
print(tampilkan_pasien())
print()

def filter_belum_bayar():
    """filter orang belum bayar sesuai abjad"""
    tl = pasien_hari_ini.copy()
    t = [x if x['bayar'] else '' for x in tl]
    return t

# print(filter_belum_bayar())

# ======
# SOAL 2
# ======

def info_klinik():
    """nama, alamat, telp"""
    return ('Klinik Sehat Bersama', "Jl. Merdeka No. 10, Pekanbaru", '0761-12345')

# Tampilkan info klinik
print("Info Klinik")
info_k = info_klinik()
print(f"Nama: {info_k[0]}")
print(f"Alamat: {info_k[1]}")
print(f"Telp: {info_k[2]}")
print()

def rekap_penyakit():
    my_dik = dict()

    tl = pasien_hari_ini.copy()
    pl = []
    for k in tl:
        pl.append(k['penyakit']) 

    p = set(pl)
    lp = len(p)

    hitung_p = {}
    for z in p:
        hitung_p.update({z:pl.count(z)}) 


    my_dik.update({"jenis":p, "jumlah":lp, "rekap":hitung_p})
    return my_dik

# Tampilkan rekap penuyakit
reka_p = rekap_penyakit()

print(f"Jenis penyakit unik: {reka_p['jenis']}")
print(f"Jumlah jenis penyakit: {reka_p['jumlah']}")
print()
print("Rekap per penyakit:")
for v in reka_p['rekap']:
    print(f"{v}: {reka_p['rekap'][v]}")
print()

# =====
# SOAL 3
# ======

class Pasien:
    def __init__(self, id, nama, penyakit):
        self.__id = id
        self.__nama = nama
        self.__penyakit = penyakit

    def tampilkan_info(self):
        print(f"ID: {self.__id}")
        print(f"Nama: {self.__nama}")
        print(f"penyakit: {self.__penyakit}")

class PasienPrioritas(Pasien):
    "prioritas Darurat atau Biasa"
    def __init__(self, id, nama, penyakit, prioritas="Biasa"):
        super().__init__(id, nama, penyakit)
        self.prioritas = prioritas

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Prioritas: {self.prioritas}")
        if self.prioritas == "Darurat" or self.prioritas == 'darurat':
            print("**Segera Tangani**")
            print()

a = Pasien('P001', 'Andi', "Flu")
a.tampilkan_info()
print()

b = PasienPrioritas('P007', 'Ghani', 'Sesak Nafas', "Darurat")
b.tampilkan_info()