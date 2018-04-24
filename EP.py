# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 13:05:09 2018

ep

@author: Victor Habib  
"""

import json

with open ("Biblioteca_oficial.json", "r") as arquivo:
    Estoque=json.loads(arquivo.read())

opcoes=["\nControle de estoque", "0 - sair", "1 - adicionar item", "2 - remover item",\
        "3 - alterar item", "4 - imprimir estoque"]

for i in opcoes:
    print(i)

acao = input ('Faça sua escolha: ')

estoque = Estoque #estoque={'item':{'quantidade': n, 'preco': x}}

while acao != "0":

    if acao == "1":
        produto = input("Nome do produto: ")
        if produto not in estoque:
            quantidade = int(input("Quantidade inicial: "))
            valor = float(input("Valor: "))
            while quantidade < 0:
                print ("A quantidade inicial não pode ser negativa.")
                quantidade = int(input("Quantidade inicial: "))
            while valor < 0:
                print (" O valor não pode ser negativo.")
                valor = float(input("Valor: "))
            if quantidade > 0:
                quantidade_produto={}
                quantidade_produto['Quantidade']=quantidade
                quantidade_produto['Valor']=valor
                estoque[produto]=quantidade_produto
                for i in opcoes:
                    print(i)
                acao = input ('Faça sua escolha: ')
        else:
            print("Produto ja cadastrado")
            for i in opcoes:
                print(i)
            acao = input ('Faça sua escolha: ')

    if acao == '2':
        remover = input ('Nome do produto: ')
        if remover in estoque:
            del estoque[remover]
            for i in opcoes:
                print(i)
            acao = input ('Faça sua escolha: ')
        else:
            print("Elemento não encontrado.")
            for i in opcoes:
                print(i)
            acao = input ('Faça sua escolha: ')

    if acao == '3':
        alterar = input ('Nome do produto: ')
        if alterar in estoque:
            quantidade=int(input('Quantidade: '))
            valor=float(input('Valor: '))
            estoque[alterar]['Quantidade'] += quantidade
            estoque[alterar]['Valor'] += valor
            for i in opcoes:
                print(i)
            acao = input ('Faça sua escolha: ')
        else:
            print("Elemento nao encontrado.")
            for i in opcoes:
                print(i)
            acao = input ('Faça sua escolha: ')
    
    if acao == "4":
        for produto in estoque:
            print("{0} : {1} valor de {0} é R${2}" .format(produto,estoque[produto]["Quantidade"],estoque[produto]["Valor"]))
        for i in opcoes:
            print(i)
        acao = input ('Faça sua escolha: ')



print("Até mais")

with open ("Biblioteca_oficial.json", "w") as arquivo:
    arquivo.write(json.dumps(estoque, sort_keys=True, indent=4))
