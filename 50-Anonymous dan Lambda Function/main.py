# Lambda Function

def f_kuadrat(angka):
    return angka**2

print(f"Hasil dari kuadrat: {f_kuadrat(5)}")

# lambda

kuadrat = lambda angka :angka**2
print(f"hasil dari lambda kuadra: {kuadrat(4)}")

pangkat = lambda num,pow : num**pow
print(f"Hasil lambda pangkat: {pangkat(2,7)}")

# sorting
data_list = ["geni", "denorma", "lamina" , "abdis"]
data_list.sort()
print(f"sorted list : {data_list}")
# sort dengan len
data_list.sort(key=len)
print(f"sorted list by len : {data_list}")

# sort dengan lambda
data_list = ["geni", "denorma", "lamina" , "abdis", "art"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda : {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka))
print(data_angka_baru)

data_angka_baru_lmbda = list(filter(lambda x:x<=6,data_angka))
print(data_angka_baru_lmbda)

# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# Kelipatan tiga
data_kelipatan3 = list(filter(lambda x:(x%3==0),data_angka))
print(data_kelipatan3)

# Anonymous function
# currying <- haskel curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(2,5)
print(f"hasil function biasa : {data_hasil}")

#  dengan currying
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"7 pangkat 2 : {pangkat2(7)}")
pangkat2 = pangkat(6)
print(f"2 pangkat 6 : {pangkat2(2)}")
print(f"Pangkat bebas: {pangkat(3)(5)}")

