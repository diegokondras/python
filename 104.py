#!/usr/bin/python3

###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.

def saoIguais(lista1, lista2):
    if (lista1 == lista2):
        return True
    else:
        return False

print(saoIguais([1, 2, 3, 4, 5], [1, 2, 3, 4 , 5]))
print(saoIguais([1, 1, 1, 1, 1], [1, 2, 3 , 4, 5]))

# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.

def palindrome(palavra1, palavra2): 
    palavra1 = palavra1.lower().replace(' ','')
    palavra2 = palavra2.lower().replace(' ','')
       
    if palavra1 == palavra2[::-1]:
        return True
    else:
        return False

print(palindrome('Omo', 'omo'))
print(palindrome('ovo', 'ovo'))
print(palindrome('casa', 'Casa'))