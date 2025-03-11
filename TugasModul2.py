#Daftar Film Yang Sedang Tayang 
print('|=================================================================================|')
print('|                        ----WELCOME TO ANDALAS CINEMA----                        |')
print('|=================================================================================|')
print('|                    --SILAHKAN PILIH FILM YANG ANDA INGINKAN--                   |')
print('|---------------------------------------------------------------------------------|')
print('|        KODE FILM       |         JUDUL FILM          |        HARGA TIKET       |')
print('|---------------------------------------------------------------------------------|')
print('|            1           |   KISAH NABI MUHAMMAD SAW   |         Rp70.000         |')
print('|            2           |   KISAH NABI ADAM AS        |         Rp55.000         |')
print('|            3           |   KISAH NABI ISA AS         |         Rp60.000         |')
print('|            4           |   KISAH NABI YUSUF AS       |         Rp50.000         |')
print('|            5           |   KISAH NABI MUSA AS        |         Rp65.000         |')
print('|=================================================================================|')

#input
Nama_Customer = input("ATAS NAMA SIAPA ?: ")
Jumlah_Tiket = int(input("MAU BERAPA TIKET ?: "))
Kode_Film = int(input("MASUKKAN KODE FILM YANG ANDA INGINKAN (1-5): "))

#Pengkondisian Kode Film
if Kode_Film == 1:
    Judul_Film = str("KISAH NABI MUHAMMAD SAW")
    Harga = int(70000 * Jumlah_Tiket)
elif Kode_Film == 2:
    Judul_Film = str("KISAH NABI ADAM AS")
    Harga = int(55000 * Jumlah_Tiket)
elif Kode_Film == 3:
    Judul_Film = str("KISAH NABI ISA AS")
    Harga = int(60000 * Jumlah_Tiket)
elif Kode_Film == 4:
    Judul_Film = str("KISAH NABI YUSUF AS")
    Harga = int(50000 * Jumlah_Tiket)
elif Kode_Film == 5:
    Judul_Film = str("KISAH NABI MUSA AS")
    Harga = int(65000 * Jumlah_Tiket)
else:
    Judul_Film = str("MOHON MAAF SAAT INI FILM TIDAK TERSEDIA")
    Harga = int(0 * Jumlah_Tiket)
    
#Diskon
if Harga > 250000:
    Diskon = int(35/100 * Harga)
elif 100000 < Harga <= 250000:
    Diskon = int(15/100 * Harga)
else:
    Diskon = int(0/100 * Harga)

#Struk Pemesanan
print("|=================================================================================|")
print("|                             ----ANDALAS CINEMA----                              |")
print("|=================================================================================|")
print("                   Nama                : ", Nama_Customer                           )
print("                   Judul Film          : ", Judul_Film                              )
print("                   Jumlah Tiket        : ", Jumlah_Tiket                            )   
print("                   Harga Satuan        :  Rp", int(Harga/Jumlah_Tiket)              )
print("                   Potongan Harga      :  Rp", Diskon                               )
print("                   Total Harga         :  Rp", Harga-Diskon                         ) 
print("|=================================================================================|")
print("|                           ----THANKYOU FOR ORDER----                            |")
print("|                             ^_^ HAPPY WATCHING ^_^                              |")
print("|=================================================================================|")



