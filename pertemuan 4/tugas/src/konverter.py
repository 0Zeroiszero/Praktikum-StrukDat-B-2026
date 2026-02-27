from decimal import Decimal

try:
    from .kurs import kurs_terhadap_idr as kurs
except ImportError:
    raise ImportError("Module 'kurs' tidak ditemukan")


def _get_daftar_kurs() -> str:
    """Mengembalikan daftar mata uang yang tersedia."""
    return ", ".join(kurs.keys())


def konversi_mata_uang(
    jumlah: Decimal, mata_uang_awal: str, mata_uang_tujuan: str
) -> Decimal:
    """
    Konversi mata uang menggunakan base currency (IDR).

    Args:
        jumlah: Jumlah uang (wajib tipe Decimal)
        mata_uang_awal: Kode mata uang asal
        mata_uang_tujuan: Kode mata uang tujuan

    Returns:
        Hasil konversi dalam tipe Decimal

    Raises:
        ValueError: Jika mata uang tidak ditemukan
    """
    # validasi
    if mata_uang_awal not in kurs:
        error = ValueError(f"Mata uang asal '{mata_uang_awal}' tidak ditemukan.")
        error.add_note(f"Daftar mata uang tersedia: {_get_daftar_kurs()}")
        raise error

    if mata_uang_tujuan not in kurs:
        error = ValueError(f"Mata uang tujuan '{mata_uang_tujuan}' tidak ditemukan.")
        error.add_note(f"Daftar mata uang tersedia: {_get_daftar_kurs()}")
        raise error

    # jika mata uang sama, kembalikan langsung
    if mata_uang_awal == mata_uang_tujuan:
        return jumlah

    # ambil nilai kurs dari variabel global
    rate_asal = kurs[mata_uang_awal]
    rate_tujuan = kurs[mata_uang_tujuan]

    # rumus: (jumlah * asal_IDR) / tujuan_IDR
    nilai_dalam_idr = jumlah * rate_asal
    hasil = nilai_dalam_idr / rate_tujuan

    return hasil
