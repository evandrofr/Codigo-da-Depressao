# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:07:03 2018

@author: Lenovo
"""
import json

with open('arquivo4.json','r') as arquivo:
    Estoque = json.loads(arquivo.read())


#print('''Controle de estoque
#0 - sair
#1 - adicionar item
#2 - remover item
#3 - alterar item
#4 - imprimir estoque
#5 - modificar preco
#6 - imprimir estoque negativo
#7 - imprimir o valor monetario''')
i=1
while i!=0:
    print('''Controle de estoque
0 - sair
1 - adicionar item
2 - remover item
3 - alterar item
4 - imprimir estoque
5 - modificar preco
6 - imprimir estoque negativo
7 - imprimir o valor monetario''')
    x=int(input('Faça sua escolha: '))
    if x==0:
        print('Até mais!')    
        i=0
    elif x==1:
        item=input('Nome do produto: ')
        item=item.lower()
        if item in Estoque:
            print('Produto já está cadastrado.')
        else:
            quant=int(input('Quantidade inicial: '))
            while quant<0:
                print('A quantidade inicial não pode ser negativa.')
                quant=int(input('Quantidade iniciail: '))
            preco=float(input('Preco do produto: '))
            while preco<0:
                print('O preco não pode ser negativo.')
                preco=float(input('Preco do produto: '))
            Estoque[item]={'Quantidade':quant}
            Estoque[item]['Preco']=preco
    elif x==2:
        item=input('Nome do produto: ')
        item=item.lower()
        if item in Estoque:
            del Estoque[item]
        else:
            print('Elemento não encontrado')
    elif x==3:
        item=input('Nome do produto: ')
        item=item.lower()
        if item in Estoque:
            quant=int(input('Quantidade: '))
            Estoque[item]['Quantidade']+=quant
        else:
            print('Elemento não encontrado')
    elif x==4:
        for k in Estoque:
               print('Produto {0}: (Quantidade: {1}, Preco: {2})'.format(k,Estoque[k]['Quantidade'],Estoque[k]['Preco']))
    elif x==5:
         item=input('Nome do produto: ')
         item=item.lower()
         if item in Estoque:
             novo_preco=float(input("Digite o novo preco:"))
             while novo_preco <0:
                 print('O preco não pode ser negativo.')
                 novo_preco=float(input("Digite o novo preco:"))
             Estoque[item]["Preco"]=novo_preco
         else:
            print("Produto nao esta no estoque")
    elif x==6:
        for produto in Estoque:
            if Estoque[produto]['Quantidade']<0:
                print('Produto {0}: (Quantidade: {1}, Preco: {2})'.format(produto,Estoque[produto]['Quantidade'],Estoque[produto]['Preco']))
    elif x==7:
        somap=0
        soman=0
        for produto in Estoque:
            if Estoque[produto]['Quantidade']>0:
                somap+=Estoque[produto]['Quantidade']*Estoque[produto]['Preco']
            elif Estoque[produto]['Quantidade']<0:
                soman+=Estoque[produto]['Quantidade']*Estoque[produto]['Preco']
        soman=round(soman,2)
        somap=round(somap,2)
        somat=round(somap+soman,2)
        print('Valor do Estoque bruto: {0}'.format(somap))
        print('Valor em debito: {0}'.format(soman))
        print('Valor total liquido:{0}'.format(somat))
        
             
print(Estoque)

Novo_estoque = json.dumps(Estoque, sort_keys = True, indent = 4)
with open('arquivo4.json','w') as arquivo:
    arquivo.write(Novo_estoque)
    