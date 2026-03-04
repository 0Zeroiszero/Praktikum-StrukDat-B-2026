def hitung_diskon(total_belanja, level_diskon: tuple, index=0):
    if total_belanja >= level_diskon[index][0]:
        kalkulasi = total_belanja * level_diskon[index][1] / 100
        hasil_kal = total_belanja - kalkulasi
        diskon = (
            f"{level_diskon[index][1]}%",
            f"{level_diskon[index][0]}",
            f"Rp{hasil_kal}",
        )
        return diskon

    return hitung_diskon(
        total_belanja=total_belanja, level_diskon=level_diskon, index=index + 1
    )
