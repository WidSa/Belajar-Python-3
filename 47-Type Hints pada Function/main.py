# Type Hints
import string
'''
Studi Kasus
def penambahan(a,b):
    hasil = a + b
    print(hasil)

penambahan(2,3)
penambahan(d,f)
'''

# penggunaan hints
def funct_with_hints(argument:int) -> int:
    hasil = 10**argument
    return hasil

HASIL = funct_with_hints(4)
print(HASIL)

def display(argument:string):
    print(argument)

display("andi")
