# Menulis file eksternal

# 1.mode with => akan membuat file baru jika tidak ada file
# dan akan menimpa/overwrite isinya jika ada file yang sudah ada

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("baris baru pertama")

# 2.mode append
with open("data_2.txt",'w',encoding="utf-8") as file:
    file.write("data kedua baris pertama")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write(" tambah append pada data 2")

# 3.mode r+ 
with open("data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris ke-1 \n")
    file.write("baris ke-2 \n")
    file.write("baris ke-3 \n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baru") # => menimpah isi text sesuai dengan panjang data

