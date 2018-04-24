# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 13:05:09 2018

ep

@author: Victor Habib  
"""

opcoes = ['\nControle de estoque', '0 - sair', '1 - adicionar item', '2 - remover item',\
        '3 - alterar item', '4 - imprimir estoque']

for i in opcoes:
    print (i)

acao = input ('Faça sua escolha: ')

estoque = {} #estoque={'item':{'quantidade': n}}

while acao != '0':

    if acao == '1':
        produto = input ('Nome do produto: ')
        quantidade = int (input ('Quantidade inicial: '))
        while quantidade < 0:
            print ('A quantidade inicial não pode ser negativa.')
            quantidade = int (input ('Quantidade inicial: '))
        if produto not in estoque:
            if quantidade > 0:
                quantidade_produto = {}
                quantidade_produto ['Quantidade'] = quantidade
                estoque [produto] = quantidade_produto
                for i in opcoes:
                    print (i)
                acao = input ('Faça sua escolha: ')
        else:
            print ('Produto já cadastrado')
            for i in opcoes:
                print (i)
            acao = input ('Faça sua escolha: ')

    if acao == '2':
        remover = input ('Nome do produto: ')
        if remover in estoque:
            del estoque [remover]
            for i in opcoes:
                print (i)
            acao = input ('Faça sua escolha: ')
        else:
            print ('Elemento não encontrado.')
            for i in opcoes:
                print (i)
            acao = input ('Faça sua escolha: ')

    if acao == '3':
        alterar = input ('Nome do produto: ')
        if alterar in estoque:
            quantidade = int (input ('Quantidade: '))
            estoque [alterar] ['Quantidade'] += quantidade
            for i in opcoes:
                print (i)
            acao = input ('Faça sua escolha: ')
        else:
            print ('Elemento nao encontrado.')
            for i in opcoes:
                print (i)
            acao = input ('Faça sua escolha: ')
    
    if acao == '4':
        for produto in estoque:
            print ("{0} : {1}".format(produto,estoque[produto]['Quantidade']))
        for i in opcoes:
            print (i)
        acao = input ('Faça sua escolha: ')
    
print ('Até mais')
