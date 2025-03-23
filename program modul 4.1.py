#untuk membersihkan output setiap kali di run
import os
os.system("cls")

#Input baris dan kolom
Baris = int(input("Masukkan Jumlah Baris: "))
Kolom = int(input("Masukkan Jumlah Kolom: "))

#Garis atas tabel
print("\n+" + "---+" * Kolom)

#Perulangan bersarang
for i in range(Baris):
    for j in range(Kolom):
        if (i+j) % 2 == 0:
            print("| X ", end="")
        else:
            print("| O ", end="")
    print("|")
    print("+" + "---+" * Kolom)