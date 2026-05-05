from rumah_sakit import QueueLinkedList


if __name__ == "__main__":
    print("=" * 30)
    print(" SISTEM ANTRIAN POLI UMUM")
    print(" RS Sehat Bersama")
    print("=" * 30, end="\n\n")

    antrian = QueueLinkedList()

    if antrian.isempty():
        print("[CEK] Apakah antrian kosong? -> YA, antrian masih kosong.", end="\n\n")
    else:
        print("[CEK] Apakah antrian kosong? -> TIDAK.", end="\n\n")

    antrian.enqueue("BUDI", "demam tinggi")
    antrian.enqueue("ANI", "batuk pilek")
    antrian.enqueue("CITRA", "sakit kepala")

    print()
    print(f"[INFO] Jumlah pasien menunggu: {antrian.size()} orang")
    print(antrian.peek())
    print()

    antrian.dequeue()
    print()

    antrian.enqueue("DODI", "nyeri perut")

    print()
    antrian.display()
    print()

    antrian.dequeue()
    print(f"[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")

    print()
    antrian.clear()

    if antrian.isempty():
        print("[CEK] Apakah antrian kosong? -> YA, antrian sudah kosong.")

    print("\nSimulasi Selesai!")
