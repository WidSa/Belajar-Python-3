import os
import CRUD as crud

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")
    print("SELAMAT DATANG DI PROGRAM")
    print("Database Perpustakaan")
    print("="*50)

    # Check Database
    crud.init_console()

    while (True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
        print("SELAMAT DATANG DI PROGRAM")
        print("Database Perpustakaan")
        print("="*58)

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")

        user_option = input("\nMasukkan Opsi: ")
        print("-"*58+"\n")

        match user_option:
            case "1": crud.read_console()
            case "2": crud.create_console()
            case "3": crud.update_console()
            case "4": crud.delete_console()

        print("-"*58+"\n")
        is_done =  input("Apakah selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print("\nAkhir Dari Progam")
