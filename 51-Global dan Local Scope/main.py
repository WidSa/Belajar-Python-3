# Global Dan Local Scope

# Global variabel
nama_global = "Benius" # => ini adalah global scope

# akses variabel global dalam function
def fungsi():
    print(f"menampilkan nama: {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,3):
    print(f"Loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan : {nama_global}")

# Local variabel
def fungsi2():
    nama_local = "Cenar" # => variabel local
fungsi2()
# print(nama_local) # => tidak dapat dipanggil/dijalankan

# contoh 1: penggunaan akses variabel
def say_hello():
    print(f"Hallo {nama}")

nama = "venia"
say_hello()

# contoh 2: merubah varaibel global
angka = 1
def ubah_angka(nilai_baru):
    global angka # fungsi ini mendapatkan akses merubah global
    angka = nilai_baru

print(f"Sebelum: {angka}")
ubah_angka(7)
print(f"Sesudah: {angka}")

# contoh 3:
angka = 0
for i in range(0,3):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 9

print(angka)
print(angka_dummy)
