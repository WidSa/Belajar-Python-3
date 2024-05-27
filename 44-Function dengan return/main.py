# Function dengan return

# function penambahan
def penambahan(a,b):
    return a + b
# function pengurangan
def pengurangan(a,b):
    return a - b
# funtion perkalian
def perkalian(a,b):
    return a * b
# function pembagian
def pembagian(a,b):
    return a / b

# function kuadrat
def kuadrat(a):
    hasil = a**2 
    return hasil

def kalkulator(angka_1, angka_2, operator):
    if operator == '+':
        return penambahan(angka_1,angka_2)
    elif operator == '-':
        return pengurangan(angka_1,angka_2)
    elif operator == 'X' or operator == 'x':
        return perkalian(angka_1,angka_2)
    elif operator == '/':
        return pembagian(angka_1,angka_2)

angka_1 =  int(input("Masukkan angaka ke-1: "))
angka_2 =  int(input("Masukkan angaka ke-2: "))
operator = input("Masukkan operator: ")

print(f"{angka_1} {operator} {angka_2} = {kalkulator(angka_1,angka_2,operator)}")

# print(f"{angka_1} + {angka_2} = {tambah(angka_1,angka_2)}")
# print(f"{angka_1} ** 2 = {kuadrat(angka_1)}")



