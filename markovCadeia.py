import numpy as np

M1 = np.array([
    [0.7,0.1],
    [0.3,0.9]
])


M10= np.linalg.matrix_power(M1, 2)

grupo_semana1= np.array([
    [0.4],
    [0.6]
])

grupo_semana11=np.matmul(M10,grupo_semana1)
print(grupo_semana11)