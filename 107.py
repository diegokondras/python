#!/usr/bin/python3

###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla.
print(dir([]))
print(dir(()))

# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
def diferencas(lista1, lista2):
    return [x for x in lista1 if x not in lista2]

print(diferencas(dir([]), dir(())))

# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py
professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}
professor3 = dict(id=28, name='Jorge Armino', idade=37)

professor1['coordenadas'] = (1111, 2222)
professor2['coordenadas'] = (3333, 4444)
professor3['coordenadas'] = (5555, 6666)

print(professor1)
print(professor2)
print(professor3)