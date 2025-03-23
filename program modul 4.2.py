#untuk membersihkan output setiap kali di run
import os
os.system("cls")

while True:
    password = input("Masukkan Password: ")

#Inisialisasi variabel pengecekan
    panjang = len(password) >= 8
    huruf_kecil = False
    huruf_besar = False
    angka = False
    karakter_khusus = False
    karakter_khusus_list = "!@#$%^&*()-_=+[]{ };:'\",.<>?/`~"

#Perulangan
    for char in password:
        if 'a' <= char <= 'z':
            huruf_kecil = True
        elif 'A' <= char <= 'Z':
            huruf_besar = True
        elif '0' <= char <= '9':
            angka = True
        elif char in karakter_khusus_list:
            karakter_khusus = True

#Cetak
    print("\n" + "="*50)
    print(f"| {'Validasi Password':^46} |")
    print("="*50)
    print(f"| {'kriteria':^29} | {'Status':^14} |")
    print("="*50)
    print(f"| Minimal 8 karakter            | {'✅' if panjang         else '❌':^13} |")
    print(f"| Minimal 1 huruf kecil         | {'✅' if huruf_kecil     else '❌':^13} |")
    print(f"| Minimal 1 huruf kapital       | {'✅' if huruf_besar     else '❌':^13} |")
    print(f"| Minimal 1 angka               | {'✅' if angka           else '❌':^13} |")
    print(f"| Minimal 1 karakter khusus     | {'✅' if karakter_khusus else '❌':^13} |")
    print("="*50)

#Jika password valid, tampilkan pesan sukses dan keluar dari perulangan
    if panjang and huruf_kecil and huruf_besar and angka and karakter_khusus:
        print("😇 Password Valid! Selamat, password Anda memenuhi kriteria!")
        break
    else:
        print("😡 Password tidak valid! Perbaiki kriteria yang masih ❌ dan coba lagi.\n")
