def cari_buku(katalog, keyword: str):
    for i in range(len(katalog)):
        try:
            daftar = katalog[i]["nama"].lower()
            daftar.index(keyword)
            return i
        except ValueError:
            pass
