# Args pada function

# def fungsi(nama,tinggi,berat):
#     print(f"{nama} punya tinggi {tinggi} dan berat badan {berat}")

# fungsi("andi",170,77)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["budi",168,87])

# Args
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("celly",156,54)

def tambah(*data):
    output = 0
    for angka in data:
        output += angka
    return output

hasil =  tambah(8, 3, 6, 9, 2, 5)
print(f"Hasil: {hasil}")

hasil = tambah(18, 63, 65)
print(f"Hasil: {hasil}")