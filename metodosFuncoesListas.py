# Métodos de Listas

lista = [1, 3, 12, 8, 2]

# append

print('Antes do append: ', lista)
lista.append(3) # add o 3 para o final da lista
print('Depois do append: ', lista)

# insert

lista.insert(2, 10) # 2 é a posicão que vc quer inserir, 10 é o elemento que vc quer inserir
print('Depois do insert: ', lista)

# extend

lista2 = [1, 2, 3]
lista.extend(lista2) # pega os elementos e joga pro final
print('Depois do extend: ', lista)

# pop

lista.pop() # ultimo elemento é excluido
print('Lista após o pop: ', lista)

lista.pop(0) # exclui o elemento no índice 0
print('Lista após o pop: ', lista)

# remove

lista.remove(3) # exclui o elemento, não o índice. Remove sempre o primeiro que ele encontra
print('Depois do remove: ', lista)

# count

print('Quantidade de 2 na lista: ', lista.count(2)) # conta quantos elementos escolhidos tem na lista

# index

print('Índice do elemento 12: ', lista.index(12)) # Mostra o índice do elemento

# sort

lista.sort() # ordena a lista de forma crescente, lista.sort(reverse=true) decrescente
print(lista)

# Funções para listas

# len

print(len(lista)) # indica quantos elementos tem na lista

# sum

print(sum(lista)) # soma os elementos da lista

# max

print('Maior elemento da lista: ', max(lista)) # maior elemento da lista

# min

print('Menor elemento da lista: ', min(lista)) # menor elemento da lista