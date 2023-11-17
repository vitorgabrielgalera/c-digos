from numpy import *

#criação de uma função que cria exercicios de soma sem receber parametros ou retornar valores
def cria_exercicio_soma():
    num_1 = random.randint(1,20)
    num_2 = random.randint(1,20)
    print(f"{num_1} + {num_2} = ")

cria_exercicio_soma()

num_1,num_2 = input("Digite dois números inteiros separados por espaços: ").split(" ")
num_1,num_2 = int(num_1), int(num_2)

#criação de uma função que soma dois numeros recebendo parametros e sem retornar valores
def exibe_soma(num_1,num_2):
    '''Função que recebe dois valores inteiros e retorna a soma desses valores'''
    soma = num_1 + num_2
    print(f"{num_1} + {num_2} = {soma}")

exibe_soma(num_1,num_2)

#criação de uma função que soma dois numeros que não recebe parametros e retorna valores
def cria_soma():
    num_1 = random.randint(1,20)
    num_2 = random.randint(1,20)
    soma = num_1 + num_2
    return soma

soma = cria_soma()
print(soma)

#criação de uma função que soma dois numeros recebendo parametros e retorna valores
def soma_num(num_1,num_2):
    '''Função que recebe dois valores inteiros e retorna a soma desses valores'''
    num_1,num_2 = input("Digite dois números inteiros separados por espaços: ").split(" ")
    num_1,num_2 = int(num_1), int(num_2)
    soma = num_1 + num_2
    return soma

soma = soma_num(num_1,num_2)
print(soma)