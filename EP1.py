# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:07:03 2018

@author: Lenovo
"""
import json

with open('arquivo.json','r') as arquivo:
    Estoque = json.loads(arquivo.read())


print('''Controle de estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque''')
i = 1
while i != 0:
    x = int(input('Faça sua escolha: '))
    if x == 0:
        print('Até mais!')    
        i = 0
    elif x == 1:
        item = input('Nome do produto: ')
        if item in Estoque:
            print('Produto já está cadastrado.')
        else:
            quant = int(input('Quantidade inicial: '))
            while quant < 0:
                print('A quantidade inicial não pode ser negativa.')
                quant = int(input('Quantidade iniciail: '))
            preco = float(input('Preco do produto: '))
            while preco<0:
                print('O preco não pode ser negativo.')
                preco = float(input('Preco do produto: '))
            Estoque[item] = {'Quantidade':quant}
            Estoque[item]['Preco']=preco
    elif x == 2:
        item = input('Nome do produto: ')
        if item in Estoque:
            del Estoque[item]
        else:
            print('Elemento não encontrado')
    elif x == 3:
        item = input('Nome do produto: ')
        if item in Estoque:
            quant = int(input('Quantidade: '))
            Estoque[item]['Quantidade'] += quant
        else:
            print('Elemento não encontrado')
    elif x == 4:
        for k in Estoque:
            print('{0}:{1}'.format(k,Estoque[k]['Quantidade']))
            
print(Estoque)

Novo_estoque = json.dumps(Estoque, sort_keys = True, indent = 4)
with open('arquivo.json','w') as arquivo:
    arquivo.write(Novo_estoque)
    
