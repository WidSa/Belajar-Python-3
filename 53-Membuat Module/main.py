# module matematika dengan import

# from matematika import tambah,kali,pangkat 
# from matematika import * 

# dengan alias
from matematika import tambah as Tam
from matematika import kali as Kal
from matematika import pangkat as Pang


hasil_tambah = Tam(1,2,3,4,5)
print(f"hasil tambah: {hasil_tambah}")

hasil_kali = Kal(1,2,3,4,5)
print(f"hasil Kali: {hasil_kali}")

hasil_pangkat = Pang(5)(3)
print(f"hasil pangkat: {hasil_pangkat}")



