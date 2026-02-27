from src import konversi_mata_uang, kurs_terhadap_idr
from tabulate import tabulate


def tampilkan_tabel_kurs():
    """Menampilkan tabel kurs mata uang menggunakan tabulate"""
    tabel = []
    for kode, nilai in kurs_terhadap_idr.items():
        if kode == "IDR":
            continue
        kurs_format = f"{nilai:,}".replace(",", ".")
        tabel.append([kode, kurs_format])

    print(
        tabulate(
            tabel,
            headers=["Kode", "Kurs"],
            tablefmt="outline",
            stralign="right",
            colalign=["left", "right"],
            disable_numparse=True,
        )
    )


def main():
    print("=== KONVERTER MATA UANG ===\n")
    tampilkan_tabel_kurs()
    print()

    dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper().strip()
    ke = input("Ke (IDR/USD/EUR/SGD/JPY): ").upper().strip()

    try:
        jumlah = float(input("Jumlah: "))
        print()
    except ValueError:
        print("Jumlah harus berupa angka!")
        return

    hasil = konversi_mata_uang(jumlah, dari, ke)

    if hasil is None:
        print("Konversi tidak dapat dilakukan.")
    else:
        if dari == "IDR":
            print(f"Rp {jumlah:,.0f} = {hasil:.2f} {ke}".replace(",", "."))
        elif ke == "IDR":
            print(f"{jumlah} {dari} = Rp {hasil:,.0f}".replace(",", "."))
        else:
            print(f"{jumlah} {dari} = {hasil:.2f} {ke}")


if __name__ == "__main__":
    main()
