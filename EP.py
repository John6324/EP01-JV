# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:00:17 2018

@author: Victor Habib
"""

import json

with open ("Biblioteca_oficial.json", "r") as arquivo:
    lojas=json.loads(arquivo.read())
    


opcoes = ["\nControle de estoque", "0 - voltar ao controle de lojas",\
        "1 - adicionar item", "2 - remover item",\
        "3 - alterar item (quantidade ou valor)", "4 - imprimir estoque",\
        "5 - imprimir saldo total do estoque"]


controle_de_lojas = ["\nControle de loja", "0 - sair", "1 - adicionar loja", \
                    "2 - editar estoque da loja", "3 - remover loja", "4 - imprimir lojas existentes"]

for i in controle_de_lojas:
    print(i)
opcao = input("O que deseja fazer? ")


while opcao != "0":       
        
        
    if opcao == "1":
        loja = input("Escreva o nome da loja: ")
        if loja in lojas:
            print("Loja já cadastrada")
            for i in controle_de_lojas:
                print(i)
            opcao = input("O que deseja fazer? ")
        else:
            lojas[loja] = {} #lojas[loja][quantidade]=2 lojas[loja][valor]=5
            for i in controle_de_lojas:
                print(i)
            opcao = input("O que deseja fazer? ")            
            
            
    elif opcao == "2":
        loja = input("Qual loja deseja editar? ")
        if loja in lojas:
            for i in opcoes:
                print(i)
            acao = input("Faça sua escolha: ")
            
            while acao != "0":

                if acao == "1":
                    produto = input("Nome do produto: ")
                    if produto not in lojas[loja]:
                        lojas[loja][produto]={}
                        
                        quantidade = int(input("Quantidade inicial: "))
                        while quantidade < 0:
                            print("A quantidade não pode ser negativa")
                            quantidade = int(input("Quantidade inicial: "))
                        lojas[loja][produto]["Quantidade"]=quantidade
                        
                        valor = float(input("Valor: "))
                        while valor < 0:
                            print (" O valor não pode ser negativo.")
                            valor = float(input("Valor: "))
                        lojas[loja][produto]["Valor"]=valor
                        
                        for i in opcoes:
                            print(i)
                        acao = input ('Faça sua escolha: ')
                    else:
                        print("Produto já cadastrado")
                        for i in opcoes:
                            print(i)
                        acao = input ('Faça sua escolha: ')
                
                if acao == '2':
                    produto = input ('Nome do produto: ')
                    if produto in lojas[loja]:
                        del lojas[loja][produto]
                        for i in opcoes:
                            print(i)
                        acao = input ('Faça sua escolha: ')
                    else:
                        print("Produto não encontrado.")
                        for i in opcoes:
                            print(i)
                        acao = input ('Faça sua escolha: ')
            
                if acao == '3':
                    produto = input ('Nome do produto: ')
                    if produto in lojas[loja]:
                        quantidade=int(input('Quantidade a somar : '))
                        valor=float(input('Valor novo: '))
                        lojas[loja][produto]['Quantidade'] += quantidade
                        while valor < 0:
                            valor = float(input("Valor novo: "))
                        lojas[loja][produto]['Valor'] = valor
                        for i in opcoes:
                            print(i)
                        acao = input ('Faça sua escolha: ')
                    else:
                        print("Produto não encontrado.")
                        for i in opcoes:
                            print(i)
                        acao = input ('Faça sua escolha: ')
                  
            
                if acao == "4":
                    for produto in lojas[loja]:
                        print("{0}: {1} : {2} valor de {1} é R${3}" .format(loja,produto,lojas[loja][produto]["Quantidade"],lojas[loja][produto]["Valor"]))
                        for i in opcoes:
                            print(i)
                        acao = input ('Faça sua escolha: ')
                    
                if acao == "5":
                    valor_total = 0
                    for produto in lojas[loja]:
                        valor=lojas[loja][produto]["Quantidade"] * lojas[loja][produto]["Valor"]
                        valor_total = valor_total + valor
                    print("Saldo total do estoque é R${0}".format(valor_total))
                    for i in opcoes:
                        print(i)
                    acao = input ('Faça sua escolha: ')
                    
            if acao == "0":
                for i in controle_de_lojas:
                    print(i)
                opcao = input("O que deseja fazer? ") 
                    
    elif opcao == "3":
        loja=input('Qual loja deseja remover? ')
        if loja in lojas:
            del lojas[loja]
        else:
            print("Loja não cadastrada")
        for i in controle_de_lojas:
            print(i)
        opcao = input("O que deseja fazer? ")
        
    elif opcao == "4":
        for loja in lojas:
            print(loja)
        if loja not in lojas:
            print("Não há lojas cadastradas.")
        for i in controle_de_lojas:
            print(i)
        opcao = input("O que deseja fazer? ")        
            
print("Até mais")

with open ("Biblioteca_oficial.json", "w") as arquivo:
    arquivo.write(json.dumps(lojas, sort_keys=True, indent=4))
