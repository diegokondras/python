#!/usr/bin/python3

###
## Exercicios
###

# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao. Utilize a clausula else no loop implementado.
professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

def define_default_city(state):
    with open('capitais-BR.csv') as file:
        linhas = [line.rstrip() for line in file]
        for linha in linhas:
            state_file, city = linha.split(';')
            if state == state_file:
                professor1['city_origin'] = city
                return True
        else:
            return False

if define_default_city(professor1['state_origin']):
    print(professor1['city_origin'])
else:
    print('Cidade não encontrada.')

# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah robusta o suficiente.
if define_default_city(professor1['state_origin']):
    print(professor1['city_origin'])
else:
    print('Cidade não encontrada.')

# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro.
def cpfsUnicos():
    cpfs_unicos = {}
    with open('lista-cpf.txt') as file:
        linhas = [line.rstrip() for line in file]
        for linha in linhas:
            cpfs_unicos[linha] = cpfs_unicos.get(linha, 0) + 1

    with open('lista-cpf-unicos.txt', 'w') as f_saida:
        for cpf in cpfs_unicos:
            f_saida.write(cpf)

    return len(cpfs_unicos)

print(cpfsUnicos())