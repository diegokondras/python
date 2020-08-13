#!/usr/bin/python3

###
# Exercicios
###

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string
titulo1, autor_ano1 = book1.split(" by ")
titulo2, autor_ano2 = book2.split(" by ")
titulo3, autor_ano3 = book3.rsplit(" by ", 1)

# 2) Salve o titulo de cada livro em uma variável
print(titulo1)
print(titulo2)
print(titulo3)

# 3) Quantos caracteres cada título tem?
print(len(titulo1))
print(len(titulo2))
print(len(titulo3))


# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
autor1, ano1 = autor_ano1.split(', ')
autor2, ano2 = autor_ano2.split(', ')
autor3, ano3 = autor_ano3.split(', ')
print('{} - {}, {}'.format(titulo1, autor1, ano1))
print('{} - {}, {}'.format(titulo2, autor2, ano2))
print('{} - {}, {}'.format(titulo3, autor3, ano3))


# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta
palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

palindrome_one = palindrome_one.replace(' ', '')
palindrome_two = palindrome_two.replace(' ', '')
palindrome_three = palindrome_three.replace(' ', '')
palindrome_four = palindrome_four.replace(' ', '')

palindrome_one = palindrome_one.lower()
palindrome_two = palindrome_two.lower()
palindrome_three = palindrome_three.lower()
palindrome_four = palindrome_four.lower()

string1 = palindrome_one[::-1]
if string1 == palindrome_one:
    print('Verdadeiro')

string2 = palindrome_two[::-1]
if string2 == palindrome_two:
    print('Verdadeiro')

string3 = palindrome_three[::-1]
if string3 == palindrome_three:
    print('Verdadeiro')

string4 = palindrome_four[::-1]
if string4 == palindrome_four:
    print('Verdadeiro')
else:
	print('Falso')