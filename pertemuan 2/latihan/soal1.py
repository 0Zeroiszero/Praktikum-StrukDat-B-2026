angka = [10, 20, 30, 40, 50]
angka.append(60)
angka.remove(20)
tertinggi = max(angka)
terendah = min(angka)
rata = sum(angka) / len(angka)

print(f"Tertinggi = {tertinggi}, Terendah = {terendah}, Rata-rata = {rata}")
print(f"Seluruh perubahan list = {angka}")
