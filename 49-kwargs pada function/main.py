# KWargs

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("deni",168,78)

def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(nama="veni",tinggi=181,berat=87)

# studi kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operasi")

    return output


hasil = math(2,4,6,8,10,option="tambah")
print(f"Hasil Penjumlahan: {hasil}")

hasil = math(3,5,7,option="kali")
print(f"Hasil Perkalian: {hasil}")

