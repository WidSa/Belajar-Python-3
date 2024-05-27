# Latihan Function
import os

"""
# Program menghirung persegi 
# Header program
os.system("clear")
print(f"{'Program Menghitung Luas':^53}")
print(f"{'Dan Keliling Persegi Panjang':^55}")
print(f"{'='*50}")

# Input User
LEBAR = int(input("Masukkan nilai Lebar: ")) 
PANJANG = int(input("Masukkan nilai Panjang: ")) 

# Menghitung luas
LUAS = PANJANG * LEBAR
KELILING = 2*(PANJANG + LEBAR)

# Tampilan Hasil
print(f"Hasil Perhitungan Luas: {LUAS}")
print(f"Hasil Perhitungan Keliling: {KELILING}") """

def header():
    os.system("clear")
    print(f"{'Program Menghitung Luas':^53}")
    print(f"{'Dan Keliling Persegi Panjang':^55}")
    print(f"{'='*50}")

def input_user():
    Lebar = int(input("Masukkan nilai Lebar: ")) 
    Panjang = int(input("Masukkan nilai Panjang: ")) 
    return Lebar, Panjang

def Perhitungan_Luas(Lebar, Panjang):
    return Panjang*Lebar

def Perhitungan_Keliling(Lebar, Panjang):
    return 2*(Panjang + Lebar)

def display(massage, value):
    print(f"Hasil Perhitungan {massage}: {value}")


def option_perhitungan():
    Pilihan = input("\nIngin menghitung Luas/Keliling (L/K) Persegi? ")
    if Pilihan == 'L' or Pilihan == 'l':
        return display("Luas",LUAS)
    elif Pilihan == 'K' or Pilihan == 'k':
        return display("Keliling",KELILING)
    else:
        print("Silahkan masukkan sesuai pilihan (L/K)")
        option_perhitungan() 

while True:
    header()
    LEBAR, PANJANG = input_user()
    LUAS = Perhitungan_Luas(LEBAR,PANJANG)
    KELILING = Perhitungan_Keliling(LEBAR,PANJANG)

    option_perhitungan()    

    isContinue = input("\nApakah lanjut (y/n)? ")
    if isContinue == 'n' or isContinue == 'N':
        break


print("\nAkhir dari Program")