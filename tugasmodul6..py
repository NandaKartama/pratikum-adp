# Konversi nilai huruf ke angka
konversi_nilai = {
    "A": 4.00, "A-": 3.75, "B+": 3.50, "B": 3.00,
    "B-": 2.75, "C+": 2.50, "C": 2.00, "D": 1.00, "E": 0.00
}

# Input jumlah mahasiswa dan mata kuliah
jumlah_mhs = int(input("Masukkan jumlah mahasiswa: "))
jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

# Simpan data IP mahasiswa
data_nilai = []

# Input nilai per mahasiswa
for i in range(jumlah_mhs):
    nama = input(f"\nMasukkan nama mahasiswa ke-{i+1}: ")
    nilai_matkul = []
    print(f"Masukkan nilai huruf untuk {jumlah_matkul} mata kuliah:")
    for j in range(jumlah_matkul):
        while True:
            nilai = input(f"mata kuliah ke-{j+1}: ").upper()
            if nilai in konversi_nilai:
                nilai_matkul.append(konversi_nilai[nilai])
                break
            else:
                print("Nilai tidak valid, silahkan coba lagi!")
    ip = sum(nilai_matkul) / jumlah_matkul
    data_nilai.append([nama, ip])

# Urutkan data berdasarkan IP tertinggi
data_nilai = sorted(data_nilai, key=lambda x: x[1], reverse=True)

# Tampilkan tabel
print("\nTABEL IP MAHASISWA")
print("=" * 35)
print(f"{'Nama':<20} {'IP':>5}")
print("=" * 35)
for nama, ip in data_nilai:
    print(f"{nama:<20} {ip:>5.2f}")