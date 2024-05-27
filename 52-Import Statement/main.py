# Import Statement
# berfungsi untuk mengambil program dari file eksternal .py 

# 1. untuk menyambung program dari eksternal
import program_print

# 2. import dengan data
import variabel

# data ada di namespace variabel
print(variabel.data)

# 3. import dengan function
import penjumlahan

hasil = penjumlahan.tambah(7,8)
print(f"hasil: {hasil}")