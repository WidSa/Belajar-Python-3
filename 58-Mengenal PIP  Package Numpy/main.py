# Packaage Numpy
import numpy as np 

list_A =[1,3,5,7]
vector_A = np.array([2,4,6,8])

print(list_A)
print(f"List_a : {list_A}")
print(f"Jika list_A*2: {list_A*2}")

print(list_A)
print(f"vector_A : {vector_A}")
print(f"Jika vector_A*2: {vector_A*2}")

matrix_2d = np.array([(3,5),(2,4)])
print(f"matrix: \n{matrix_2d}")
print(f"matrix*2: \n{matrix_2d*2}")

zeros_c = np.zeros((2,2))
print(f"Zeros c: \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"Ones d: \n{ones_d}")

jumlah_matrix = matrix_2d + (matrix_2d*2) + ones_d
print(f"jumlah: \n{jumlah_matrix}")
