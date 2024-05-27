# tutorial membaca file eksternal

print("="*10, " Membaca File Eksternal ", "="*10)

file = open("data.txt",mode="r")
print(f"status read: {file.readable()}")
print(f"status read: {file.writable()}")

# baca seluruh file
print(file.read())

# baca perbaris
# print(file.readline()) # membaca baris pertama(perbaris)
# print(file.readline()) # membaca baris kedua(perbaris)

# baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah diclose: {file.closed}")
file.close()
print(f"apakah file sudah diclose: {file.closed}\n")

# membaca file dengan with
print("="*7, "Membaca File Eksternal dengan With", "="*7 )

with open("data.txt",mode="r") as file:
    # content = file.readline()
    content = file.read()
    print(content)
    # print(content,end="")
    print(f"apakah file sudah diclose: {file.closed}")

print(f"apakah file sudah diclose: {file.closed}")


