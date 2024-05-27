from . import Operasi

def create_console():
    print("\n"+"="*55)
    print("Silahkan Tambahkan Data Buku Baru\n")
    judul = input("Judul\t: ")
    penulis = input("Penulis\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus berupa angka!!! \nsilahkan masukkan tahunnya lagi (yyyy)")
        except:
            print("Tahun harus berupa angka!!! \nsilahkan masukkan tahunnya lagi (yyyy)")
    Operasi.crete(penulis,judul,tahun)
    print("-"*58+"\n")
    print("Berikut adalah Data baru anda")
    print(f"Penulis\t: {penulis:.15}")
    print(F"Judul\t: {judul:.25}")
    print(f"Tahun\t: {tahun:4}")

def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*58)
    print(f"{index:4} | {judul:25} | {penulis:15} | {tahun:4}")
    print("-"*58+"\n")
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.25} | {penulis:.15} | {tahun:4}",end="")
        
    # Footer
    print("="*58+"\n")

def update_console():
    read_console()
    while(True):
        print("Silahkan pilih Buku yang akan di update!")
        no_buku =  int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            break
        else:
            print("Nomor tidak valid, Silahkan masukkan lagi")

    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        # data yang ingin diubah
        print("\n"+"="*58)
        print("Silahkan pilih data apa yang ingin anda rubah")
        print(f"1. Penulis\t: {penulis:.15}")
        print(F"2. Judul\t: {judul:.25}")
        print(f"3. Tahun\t: {tahun:4}")
        print("-"*58+"\n")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n")
        match user_option:
            case "1": penulis = input("Penulis\t: ")
            case "2": judul = input("Judul\t: ")
            case "3": 
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus berupa angka!!! \nsilahkan masukkan tahunnya lagi (yyyy)")
                    except:
                        print("Tahun harus berupa angka!!! \nsilahkan masukkan tahunnya lagi (yyyy)")
            case _: print("Pilihan tidak ada !!!")

        print("Data Baru anda")
        print(f"1. Penulis\t: {penulis:.15}")
        print(F"2. Judul\t: {judul:.25}")
        print(f"3. Tahun\t: {tahun:4}")
        print("-"*58+"\n")
        is_done =  input("Apakah data sudah sesuai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
    Operasi.update(no_buku,pk,data_add,penulis,judul,tahun)

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih Buku yang akan di delete!")
        no_buku =  int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            print("\n"+"="*58)
            print("Berikut adalah data yang ingin anda Hapus\n")
            print(f"Penulis\t: {penulis:.15}")
            print(F"Judul\t: {judul:.25}")
            print(f"Tahun\t: {tahun:4}")
            print("-"*58+"\n")

            is_done =  input("Yakin data ini yang akan dihapus (y/n)? ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor tidak valid, Silahkan masukkan lagi")
    print("Data Berhasil Dihapus")
    