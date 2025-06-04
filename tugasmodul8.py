def tambah():
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    kelas = input("Masukkan kelas: ")
    pengalaman = input("Masukkan pengalaman (pisahkan dengan ;, tambah (Ketua) jika pernah jadi ketua): ")
    wawancara = input("Masukkan nilai wawancara (0-100): ")
    pilihan = input("Masukkan pilihan bidang (Acara/Pubdok/Perlengkapan/Danus): ")

    with open("OrPSB22.txt", "a") as file:
        file.write(f"{nama}, {nim}, {kelas}, {pengalaman}, {wawancara}, {pilihan}\n")

    print("\n<<!! DATA BARU ANDA BERHASIL DITAMBAHKAN !!>>\n")

def hapus(nama):
    with open("OrPSB22.txt", "r") as file:
        lines = file.readlines()

    with open("OrPSB22.txt", "w") as file:
        for line in lines:
            if not line.startswith(nama + ","):
                file.write(line)

    print("\n<<!! DATA LAMA ANDA BERHASIL DIHAPUSKAN !!>>\n")

def tampilkan():
    try:
        with open("OrPSB22.txt", "r") as file:
            lines = file.readlines()
            if lines:
                print("\nData Cakoors:")
                for line in lines:
                    print(line.strip())
            else:
                print("Oppss. Data kosong. Silakan tambah data dulu ya ^_^")
    except FileNotFoundError:
        print("File data belum ditemukan. Silakan tambah data dulu ya ^_^")

def parse_pengalaman(pengalaman_str):
    pengalaman = []
    ketua = []
    for item in pengalaman_str.split(";"):
        item = item.strip()
        if "(Ketua)" in item:
            bidang = item.replace("(Ketua)", "").strip()
            pengalaman.append(bidang)
            ketua.append(bidang)
        else:
            pengalaman.append(item)
    return pengalaman, ketua

def proses_seleksi():
    from collections import defaultdict
    try:
        with open("OrPSB22.txt", "r") as file:
            lines = file.readlines()

        data_per_bidang = defaultdict(list)

        for line in lines:
            if not line.strip():
                continue
            nama, nim, kelas, pengalaman_str, wawancara_str, pilihan = map(str.strip, line.strip().split(","))
            wawancara = float(wawancara_str)
            pengalaman, ketua_bidang = parse_pengalaman(pengalaman_str)

            poin = 0
            if pilihan in pengalaman:
                poin += 3
            if pilihan in ketua_bidang:
                poin += 2

            nilai_cakoor = wawancara + poin
            data_per_bidang[pilihan].append({
                "nama": nama,
                "nim": nim,
                "kelas": kelas,
                "nilai": nilai_cakoor
            })

        hasil = []
        for bidang, daftar in data_per_bidang.items():
            hasil.append(f"Bidang: {bidang}")
            top2 = sorted(daftar, key=lambda x: x["nilai"], reverse=True)[:2]
            for i, orang in enumerate(top2, 1):
                hasil.append(f"  {i}. {orang['nama']} ({orang['nim']}, {orang['kelas']}) - Nilai: {orang['nilai']}")
            hasil.append("")

        with open("HasilSeleksiKoordinator.txt", "w") as out:
            out.write("\n".join(hasil))

        print("\n<<!! HASIL SELEKSI BERHASIL DIPROSES DAN DISIMPAN DI 'HasilSeleksiKoordinator.txt' !!>>")
    except Exception as e:
        print("Terjadi kesalahan saat memproses seleksi:", e)

# Main Menu
while True:
    print("\nLayanan Sistem Seleksi Cakoor:")
    print("1. Menambahkan data cakoors baru")
    print("2. Menghapus data berdasarkan nama")
    print("3. Menampilkan semua data")
    print("4. Proses seleksi koordinator")
    print("5. Selesai")

    pilihan = input("Apa yang ingin kamu lakukan? (1-5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        nama = input("Masukkan nama yang ingin dihapus: ")
        hapus(nama)
    elif pilihan == "3":
        tampilkan()
    elif pilihan == "4":
        proses_seleksi()
    elif pilihan == "5":
        print("Terima kasih sudah menggunakan layanan ini :)")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")