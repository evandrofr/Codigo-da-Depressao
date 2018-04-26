# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:07:03 2018

@author: Lenovo
"""
#print('''Controle de estoque
#0 - sair
#1 - adicionar item
#2 - remover item
#3 - alterar item
#4 - imprimir estoque
#5 - modificar preco
#6 - imprimir estoque negativo
#7 - imprimir o valor monetario''')
from firebase import firebase 
firebase = firebase.FirebaseApplication('https://ep-evandro-giovanna-leo.firebaseio.com/', None)

import json

with open('arquivo5.json','r') as arquivo:
    Estoque = json.loads(arquivo.read())
i=1
while i!=0:    
    print('''Controle de loja:
        0 - sair
        1 - Acessar uma loja 
        2 - Adicionar loja 
        3 - Excluir loja''')
    y = int(input('Faca sua escolha: '))
    if y == 0:
        i = 0
    elif y == 1:
        print('Lojas disponiveis: ')
        for k in Estoque:
            print(k)
        loja = input('Qual loja deseja acessar? ')
        loja = loja.lower()
        if loja not in Estoque:
            print('Loja indisponivel')
        else:
            i = 1
            while i != 0:
                print('''Controle de estoque da loja {0}:
                      0 - sair
                      1 - adicionar item
                      2 - remover item
                      3 - alterar item
                      4 - imprimir estoque
                      5 - modificar preco
                      6 - imprimir estoque negativo
                      7 - imprimir o valor monetario'''.format(loja))
                x = int(input('Faça sua escolha: '))
                if x == 0:
                    print('Até mais!')    
                    i = 0
                elif x == 1:
                    item = input('Nome do produto: ')
                    item = item.lower()
                    if item in Estoque[loja]:
                        print('Produto já está cadastrado.')
                    else:
                        quant = int(input('Quantidade inicial: '))
                        while quant<0:
                            print('A quantidade inicial não pode ser negativa.')
                            quant = int(input('Quantidade iniciail: '))
                        preco = float(input('Preco do produto: '))
                        while preco<0:
                            print('O preco não pode ser negativo.')
                            preco = float(input('Preco do produto: '))
                        Estoque[loja][item] = {'Quantidade':quant}
                        Estoque[loja][item]['Preco'] = preco
                elif x == 2:
                    item = input('Nome do produto: ')
                    item = item.lower()
                    if item in Estoque[loja]:
                        del Estoque[loja][item]
                    else:
                        print('Elemento não encontrado')
                elif x == 3:
                    item = input('Nome do produto: ')
                    item = item.lower()
                    if item in Estoque[loja]:
                        quant = int(input('Quantidade: '))
                        Estoque[loja][item]['Quantidade'] += quant
                    else:
                        print('Elemento não encontrado')
                elif x == 4:
                    for k in Estoque[loja]:
                        print('Produto {0}: (Quantidade: {1}, Preco: {2})'.format(k,Estoque[loja][k]['Quantidade'],Estoque[loja][k]['Preco']))
                elif x == 5:
                    item = input('Nome do produto: ')
                    item = item.lower()
                    if item in Estoque[loja]:
                        novo_preco = float(input("Digite o novo preco:"))
                        while novo_preco <0:
                            print('O preco não pode ser negativo.')
                            novo_preco = float(input("Digite o novo preco:"))
                        Estoque[loja][item]["Preco"] = novo_preco
                    else:
                        print("Produto nao esta no estoque")
                elif x == 6:
                    for produto in Estoque[loja]:
                        if Estoque[loja][produto]['Quantidade'] < 0:
                            print('Produto {0}: (Quantidade: {1}, Preco: {2})'.format(produto,Estoque[loja][produto]['Quantidade'],Estoque[loja][produto]['Preco']))
                elif x == 7:
                    somap = 0
                    soman = 0
                    for produto in Estoque[loja]:
                        if Estoque[loja][produto]['Quantidade'] > 0:
                            somap += Estoque[loja][produto]['Quantidade'] * Estoque[loja][produto]['Preco']
                        elif Estoque[loja][produto]['Quantidade'] < 0:
                            soman += Estoque[loja][produto]['Quantidade']*Estoque[loja][produto]['Preco']
                    soman = round(soman,2)
                    somap = round(somap,2)
                    somat = round(somap+soman,2)
                    print('Valor do Estoque bruto: {0}'.format(somap))
                    print('Valor em debito: {0}'.format(soman))
                    print('Valor total liquido:{0}'.format(somat))
    
    elif y == 2:
        loja = input('Qual o nome da loja a adicionar? ')
        if loja in Estoque:
            print('Loja já existente')
        else:
            Estoque[loja] = {}
    elif y == 3:
        loja = input('Qual loja gostaria de excluir? ')
        if loja in Estoque:
            del Estoque[loja]
            print('Loja {0} Excluida'.format(loja))
        else:
            print('Loja inexistente')
            
             
print(Estoque)

Novo_estoque = json.dumps(Estoque, sort_keys = True, indent = 4)
with open('arquivo5.json','w') as arquivo:
    arquivo.write(Novo_estoque)
firebase.put('/pasta',"Estoque",Estoque)
    
