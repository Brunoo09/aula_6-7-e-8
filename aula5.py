# # identação
# # é sobre capsular corretamente
# # os blocos de códigos

# # concatenação
# # juntar dados

# nome = 'brunao'
# print(f'ola''{nome}')

# #.format
# nome = 'paula'
# print('ola {}'.format(nome))

# #+
# nome = 'pedro'
# print('ola'  + '' + nome)

# print('ola \n mundao')

# #refatoração

# #bug impede de funcionar como planejado
# #erro impede o código de funcionar

# n1 = int(input(':'))
# n2 = int(input(':'))

# soma = n1 +n2
# print(soma)


lista = [1,2,3,4,5,6]

# lista.clear()

nova_lista = lista.copy()


print(nova_lista)

# n1 = lista[0]
# n2 = lista[1]

# lista[0] = 25
# lista[1] = 12

# lista.append(10)
# lista.append('test')

# del lista[3]
# lista.remove(5)
# lista.pop()

# lista +=(10,2030,50,6,6)
# lista.extend([1,2,3,6,6])

# soma = n1 + n2
# print(lista)

# lista.insert(3,7)
# print(lista)

# lista2 = list(range(1,151))
# print(lista2)
# numero = int(input('busque o valor'))
#  lista[12,4246,358275,15,30]


# Exercício 1: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

# lista = list(range(2,21))
# print(lista)

# # Exercício 2: Escreva um programa que use a função range() para gerar os múltiplos de 5 em 5 até 50, em seguida, calcule e imprima a soma desses múltiplos.

# lista = list(range(5,50,5))
# print(lista)

# # **Exercício 1:** Crie uma lista chamada pessoas que contenha os números inteiros de pessoa1 a pessoa5 e imprima-a na tela.

# pessoas = ['pessoa1', 'pessoa2', 'pessoa3', 'pessoa4', 'pessoa5']
# print(pessoas)

# # **Exercício 2:** Acesse e imprima o terceiro elemento da lista `numeros`.

# lista = [1,2,3,4,5,6,7,8,9,10]
# print(lista[3])

# # Exercício 3: Adicione o número 9 à lista numeros e imprima a lista atualizada

# lista.insert(2,9)
# print(lista)

# # **Exercício 4:** Remova o número 5 da lista `numeros` e imprima a lista resultante.

# lista.remove(5)
# print(lista)

# # **Exercício 5:** Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista `numeros` e imprima o resultado.

# carros = ['fiesta', 'gol', 'brasilia']
# print(carros[1],lista[4])

# print('mercado')
# produtos = ['arroz', 'feijão', 'macarrão', 'molho']
# valores = [10.0, 15.00,8.00,3.50]
# carrinho =[]
# meu_valores =[]

# produtos1 = (input('''
# 1 - arroz 
# 2 - feijão
# 3 - macarrão
# 4 - molho
# >>'''))

# produtos2 = int(input('''
# 1 - arroz 
# 2 - feijão
# 3 - macarrão
# 4 - molho
# >>'''))

# carrinho = [produtos[produtos1], produtos[produtos2]]
# meu_valores =[meu_valores[produtos1], meu_valores[produtos2]]
# soma = sum(meu_valores)

# pessoa = {
# 'nome': 'paula',
# 'idade':25,
# 'endereço': 'rua 10',
# 'email': 'paula@gmail.com',
# 'curso':'python 60',

# }

# # se condiçao == true:
# #     faça isso

# if 35>=45:
#     print('é maior')

# else:
#     print('é menor')

# import random

# numero_aleatorio = random.randint(1,10)
# chute = int(input('escolha um numero: '))

# if numero_aleatorio == chute:
#     print('acertoou')
#     print('é o numero', numero_aleatorio)
# else:    
#      print('errooou', numero_aleatorio)

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

numero = int(input('digite um numero'))
if numero > 0:
    print('é positivo')
else:
    print('é negativo')

# 2*
# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

idade = int(input('digite sua idade:'))
if idade > 0:
    print('autorizado')
else:
    print('não autorizado')
