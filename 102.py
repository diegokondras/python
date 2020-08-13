#!/usr/bin/python3

###
# Exercicios
###

days_list = ['mon','tues','wed','thurs','fri']

# Como selecionar 'wed' pelo indice?
print(days_list[2])

# Como verificar o tipo de 'mon'?
print(type(days_list[0]))

# Como separar 'wed' até 'fri'?
print(days_list[2:5])

# Quais as maneiras de selecionar 'fri' por indice?
print(days_list[4])
print(days_list[4:5])

# Qual eh o tamanho dos dias e days_list?
print(len(days_list[0]))
print(len(days_list[1]))
print(len(days_list[2]))
print(len(days_list[3]))
print(len(days_list[4]))
print(len(days_list))

# Como inverter a ordem dos dias?
days_list = ['mon','tues','wed','thurs','fri']
print(days_list[::-1])

days_list.reverse()  
print(days_list) 

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
days_list = ['mon','tues','wed','thurs','fri']
days_list.insert(1,'zero')
print(days_list)

# Como limpar list?
days_list = ['mon','tues','wed','thurs','fri']
days_list.clear() 
print(days_list) 

# Como deletar list?
days_list = ['mon','tues','wed','thurs','fri']
del days_list

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
days_list = ['mon','tues','wed','thurs','fri']
ultimo_elemento = days_list.pop()
print(days_list)
print(ultimo_elemento)