""" 
Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector 
con datos leídos por el teclado. Copia los elementos del vector en otro vector 
pero en orden inverso, y muéstralo por la pantalla.
"""

# Inicializar variables
lista = []
invertida = []
nombre = ""

for i in range(5):
    nombre = input(f"Nombre {i+1}: ")
    lista.append(nombre)

# Invertir elementos de vector
"""
Con método de listas
invertida = reverse(lista)
"""

""" 
Con implementación propia
"""
for i in range(4, -1, -1):
    invertida.append(lista[i])


# Imprimir elementos de vector invertido
print(f"Lista invertida: {invertida}")