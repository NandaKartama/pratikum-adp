#input
M = int(input("Masukkan Modal Awal: "))
r = float(input("Masukkan Suku Bunga Tahunan (%): "))
T = int(input("Masukkan Target Investasi: "))

#perulangan
tahun = 0
while M<T:
    M += M * (r/100)
    tahun += 1
    print(f"Tahun ke-{tahun}: Rp{int(M)}")
print(f"Target tercapai dalam {tahun} tahun!")