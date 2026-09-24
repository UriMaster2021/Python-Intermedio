A ={1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#1)Dados dos conjuntos, A y B, escribe un programa en Python que imprima los elementos que se encuentran en A o en B, o en ambos.
print(A.union(B))

#2)Dados dos conjuntos, A y B. escribe un programa en Python que imprima los elementos que se encuentran en A y en B
print(A.intersection(B))

#3)Dados dos conjuntos, A y B, escribe un programa en Python que imprima el conjunto de los elementos que se encuentran en A o en B, pero no en ambos.
print (A.symmetric_difference(B))

#4)Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es un subconjunto de otro conjunto, B.
if A.issubset(B):
    print("A es un subconjunto de B")
else:
    print("A no es un subconjunto de B")

#5)Dados un conjunto, A, escribe un programa en Python que imprima el número de elementos del conjunto.
print(len(A))