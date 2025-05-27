import os
os.system("cls")

# Fungsi untuk menghitung kecepatan akhir dan jarak tempuh pada GLBB
def hitung_kecepatan_jarak(v_awal, a, t):
    v_akhir = v_awal + a * t                    # Rumus kecepatan akhir
    jarak = v_awal * t + 0.5 * a * t ** 2       # Rumus jarak tempuh
    return v_akhir, jarak

print("PROGRAM MENGHITUNG KECEPATAN AKHIR DAN JARAK TEMPUH (GLBB)")
print("-" * 60)

n = int(input("Masukkan jumlah input (n): "))

hasil_perhitungan = []

# Input dan perhitungan
for i in range(n):
    print(f"\nData ke-{i+1}")
    v0 = float(input("  Kecepatan awal (m/s): "))
    a = float(input("  Percepatan (m/s²): "))
    t = float(input("  Waktu (s): "))

    v_akhir, jarak = hitung_kecepatan_jarak(v0, a, t)
    hasil_perhitungan.append((v0, a, t, v_akhir, jarak))

# Tabel hasil
print("\nHasil Perhitungan:")
print("-" * 85)
print("{:<5} {:<15} {:<15} {:<10} {:<18} {:<15}".format(
    "n", "Kecepatan Awal", "Percepatan", "Waktu", "Kecepatan Akhir", "Jarak Tempuh"
))
print("-" * 85)

for i in range(n):
    v0, a, t, v, s = hasil_perhitungan[i]
    print("{:<5} {:<15.2f} {:<15.2f} {:<10.2f} {:<18.2f} {:<15.2f}".format(
        i+1, v0, a, t, v, s
    ))

print("-" * 85)