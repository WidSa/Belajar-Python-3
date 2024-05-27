# Expection akan terjadi saat program mengalami error saat runtime

# contoh untuk menangkap expection
"""from math import nan

input_user = int(input("Masukkan angka: "))
hasil = nan

try:
    hasil = 10/input_user
except:
    print("Input tidak boleh 0")
print(f"hasil: {hasil}")
"""

# contoh di aplikasi
"""
while(True):
    angka = int(input("Masukkan angka: "))
    try:
        hasil = 10/angka
        print(f"Hasil: {hasil}")
        is_done =  input("Lanjut (y/n)? ")
        if is_done == 'n':
            break

    except:
        print("Pembagian 0, silahkan masukkan input lagi")

print("Akhir dari Program 1")
"""

# contoh aplikasi untuk membuat file data.txt
while(True):
    try:
        with open("data.txt",'r') as file:
            print(file.read())
        break
    except:
        print("file data.txt ridak ditemukan, membuat file baru")
        with open("data.txt",'w',encoding="utf-8") as file:
            file.write("file baru")
        break

print("Akhir dari Program 2")