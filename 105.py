#!/usr/bin/python3

###
# Exercicios
###

# 1) Faca um loop para retornar: ['A','B','C']
## Usando a lista: ['a','b','c']

minuscula = ['a','b','c']
maiuscula = []

for letra in minuscula:
    maiuscula.append(letra.upper())

print(maiuscula)

# 2) Faca um loop para retornar a soma de todos os elementos da listas
## Usando os numeros: [0, 1, 3, 4, 5]

def soma(list):
	soma = 0
	for x in list:
	    soma += x
	return soma

numeros =  [0, 1, 3, 4, 5]
print(soma(numeros))

# 3) Faca um loop para retornar apenas os numeros impares

def impares(list):
	impares_lista = []
	for numero in list:
	    if numero % 2:
	         impares_lista.append(numero)
	return impares_lista

numeros =  [0, 1, 3, 4, 5]
print(impares(numeros))

## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string

texto = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
texto = texto.replace(', ', '').replace('. ', '')
texto_lista = texto.split()
cont = 0

for palavra in texto_lista:
    if len(palavra) >= 5:
        cont += 1

print(cont)

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100

print([mult for mult in range(3, 100, 3)])

# 6) Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for

def primos():
    primos_lista = []
    for numero in range(2, 10):
        primo = True
        for x in range(2, numero):
            if numero % x == 0:
                primo = False
                break
        if primo:
            primos_lista.append(numero)

    return primos_lista

print(primos())