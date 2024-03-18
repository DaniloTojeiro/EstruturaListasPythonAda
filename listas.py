# Lista

notas = [7.9, 9.7, 8.2]

# Criando Listas

lista = [] # vazia
lista = list() # função
lista = [26, 'Danilo', 3.14159, False] # diferentes tipos
lista = [10, [1, 2, 3]] # lista de lista

# Indexação e Slices

lista = [10, 'Danilo', 3.1415, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) # Ultimo elemento da lista

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3]) # Do 0 ao 3
print(lista[3:6]) # Do 3 até antes do 6
print(lista[3:])  # Do 3 até o final
print(lista[2:6:2]) # Do 2 até antes do 6 de 2 em 2

# Interações com o For

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices

print('Comprimento da lista: ', len(lista)) # len = quantidade de elementos da lista

for i in range(len(lista)):
    print(i)