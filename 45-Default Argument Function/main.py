# Default argument

# Contoh 1
def sayHello(nama = "Seia"):
    print(f"Hallo {nama}")

sayHello("Dea")
sayHello()

# Contoh 2
def massage(nama ="Cea",pesan = "Gimana kabar ?"):
    print(f"Hai {nama}, {pesan}\n")

massage("Celly","Apa kabar ?")
massage("Bob")

# Contoh 3
def hitung_pangkat(angka, pangkat = 3):
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(3,3))

hasil = hitung_pangkat(angka=7,pangkat=2)
print(hasil)

print(hitung_pangkat(angka=2))