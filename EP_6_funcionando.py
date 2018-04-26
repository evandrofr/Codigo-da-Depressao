# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:07:03 2018

@author: Evandro, Giovanna e Leonardo
"""

from firebase import firebase
firebase= firebase.FirebaseApplication('https://ep-evandro-giovanna-leo.firebaseio.com',None)
if firebase.get('pasta',None) is None: #Cria o dicionario caso nao exista
    Estoque = {}
else: #Abre o dicionario salvo no Firebase
    Estoque=firebase.get('pasta',None)
j = 1 #Variavel utilizada apenas para manter o loop do sistema
while j != 0:
    print('''Controle de loja: 
        0 - Sair do Sistema
        1 - Adicionar loja 
        2 - Excluir loja
        3 - Acessar uma loja''')
    y = int(input('Faca sua escolha: '))
    if y == 3: #Funcao de acesso a loja
        print('Lojas disponiveis: ')
        for k in Estoque: #Utilizado para printar o nome de todas as lojas
            print(k)
        loja = input('Qual loja deseja acessar? ')
        loja = loja.lower() #Para padronizar as palavras sempre minusculas
        if loja not in Estoque:
            print('Loja indisponivel')
        else:
            i=1 #Variavel utilizada para manter o loop dentro da loja
            while i != 0:
                print('''Controle de estoque da loja {0}:
                  0 - sair da loja
                  1 - adicionar item
                  2 - remover item
                  3 - alterar item
                  4 - imprimir estoque
                  5 - modificar preco
                  6 - imprimir estoque negativo
                  7 - imprimir o valor monetario'''.format(loja))
                x = int(input('Faça sua escolha: '))
                if x == 0:#Funcao para sair de loja e voltar ao menu anterior
                    print('Até mais! Você saiu da loja: {0}'.format(loja))    
                    i = 0 #Mudanca de variavel que interrompe o loop
                elif x == 1: #Funcao para adicionar itens ao estoque da loja
                    item = input('Nome do produto: ')
                    item = item.lower() #Para padronizar as palavras sempre minusculas
                    if item in Estoque[loja]: #Verificando se o item ja esta cadastrado
                        print('Produto já está cadastrado.')
                    else:
                        quant = int(input('Quantidade inicial: '))
                        while quant<=0: #Impede um valor negativo ou nulo de ser quantidade inicial
                            print('A quantidade inicial não pode ser negativa ou nula.')
                            quant = int(input('Quantidade iniciail: '))
                        preco = float(input('Preco do produto: '))
                        preco = round(preco,2) #Arredonda para duas casas decimais
                        while preco <= 0: #Impede um valor negativo ou nulo de ser preco
                            print('O preco não pode ser negativo ou nulo.')
                            preco = float(input('Preco do produto: '))
                            preco = round(preco,2) #Arredonda para duas casas decimais
                        Estoque[loja][item] = {'Quantidade':quant} #Cria o dicionario com a chave quantidade
                        Estoque[loja][item]['Preco'] = preco #Adiciona preco como chave do dicionario
                        
                        
                elif x == 2: #Funcao para remover itens do estoque da loja
                    print('Produtos disponiveis: ')
                    for k in Estoque[loja]: #Para printar todos os itens da loja, para que o usuario possa escolher qual apagar
                        print(k)
                    item = input('Nome do produto a ser removido: ')
                    item = item.lower() #Para padronizar as palavras sempre minusculas
                    if item in Estoque[loja]: #Apaga somente se o item estiver em estoque
                        del Estoque[loja][item]
                        firebase.delete('pasta/{0}'.format(loja), item)
                    else:
                        print('Elemento não encontrado')
                elif x == 3: #Funcao para Alterar a quantidade de itens. Sempre adiciona o valor escolhido
                    print('Produtos disponiveis: ')
                    for k in Estoque[loja]: #Printa os itens e suas quantidades em estoque na loja, para que o usuario possa escolher qual alterar
                        print('Produto: {0}, Quantidade: {1}'.format(k,Estoque[loja][k]['Quantidade']))
                    item = input('Nome do produto: ')
                    item = item.lower() #Para padronizar as palavras sempre minusculas
                    if item in Estoque[loja]:
                        quant = int(input('Quantidade a adicionar(positivo) ou retirar(negativo): ')) #Valor positivo para adicionar, negativo para retirar. Pode deixar o estoque negativo.
                        Estoque[loja][item]['Quantidade']+=quant #Adiciona valor na quantidade ja existente
                    else:
                        print('Elemento não encontrado')
                elif x == 4: #Funcao para printar produtos, quantidades e precos em estoque na loja
                    for k in Estoque[loja]:
                        print('Produto {0}: (Quantidade: {1}, Preco: {2})'.format(k,Estoque[loja][k]['Quantidade'],Estoque[loja][k]['Preco']))
                elif x == 5: #Funcao para modificar os precos do itens em estoque na loja. Altera o preco completamente.
                    print('Produtos disponiveis a modificar: ')
                    for k in Estoque[loja]: #Printa os itens e seus precos em estoque na loja, para que o usuario possa escolher qual alterar
                        print('Produto: {0}, Preco: {1}'.format(k,Estoque[loja][k]['Preco']))
                    item = input('Nome do produto: ')
                    item = item.lower() #Para padronizar as palavras sempre minusculas
                    if item in Estoque[loja]: 
                        novo_preco = float(input("Digite o novo preco:"))
                        novo_preco = round(novo_preco,2) #Arredonda para duas casas decimais
                        while novo_preco <= 0: #Impede um valor negativo ou nulo de ser preco
                            print('O preco não pode ser negativo ou nulo.')
                            novo_preco = float(input("Digite o novo preco:"))
                            novo_preco = round(novo_preco,2) #Arredonda para duas casas decimais
                        Estoque[loja][item]["Preco"]=novo_preco #Substitui o valor do preco no dicionario
                    else:
                        print("Produto nao esta no estoque")
                elif x == 6: #Funcao para mostrar apenas os itens que possuem quantidade negativa no estoque da loja
                    for produto in Estoque[loja]:
                        if Estoque[loja][produto]['Quantidade'] < 0:
                            print('Produto {0}: (Quantidade: {1}, Preco: {2})'.format(produto,Estoque[loja][produto]['Quantidade'],Estoque[loja][produto]['Preco']))
                elif x == 7: #Mostra o valor monetario em estoque. Mostra o valor bruto (Apenas positivos), em debito (Apenas negativo) e  o total liquido(Diferenca entre os dois anteriores)
                    somap = 0 #Soma dos valores positivos
                    soman = 0 #Soma dos valores negativos
                    for produto in Estoque[loja]:
                        if Estoque[loja][produto]['Quantidade'] > 0: #Verificando Valor Bruto
                            somap += Estoque[loja][produto]['Quantidade'] * Estoque[loja][produto]['Preco']
                        elif Estoque[loja][produto]['Quantidade'] < 0: #Verificando Valor em debito
                            soman += Estoque[loja][produto]['Quantidade'] * Estoque[loja][produto]['Preco']
                    soman = round(soman,2) #Arredonda para duas casas decimais
                    somap = round(somap,2)
                    somat = round(somap+soman,2) #Calcula diferenca para total em liquido. Detalhe que o soman ja e negativo
                    print('Valor do Estoque bruto: {0}'.format(somap))
                    print('Valor em debito: {0}'.format(soman))
                    print('Valor total liquido:{0}'.format(somat))
                else: #Caso a selecao do usuario seja diferente dos numeros indicados
                    print('Selecao invalida')
                    

    elif y==1: #Funcao para adicionar uma loja
        loja=input('Qual o nome da loja a adicionar? ')
        loja=loja.lower() #Para padronizar as palavras sempre minusculas
        if loja in Estoque: #Impede que se crie duas lojas iguais
            print('Loja já existente')
        else:
            Estoque[loja]={} #Cria o dicionario que ira servir de estoque para loja
    elif y == 2: #Funcao para excluir loja
        print('Lojas existentes: ')
        for k in Estoque:
            print(k)
        loja = input('Qual loja gostaria de excluir? ')    
        if loja in Estoque:
            del Estoque[loja]
            firebase.delete('pasta', loja)
            print('Loja {0} Excluida'.format(loja))
        else:
            print('Loja inexistente')
    elif y == 0: #Funcao para sair do sistema
        j = 0 #Mudanca de variavel para sair do loop do sistema
        print('Ate mais! Saindo do Sistema!')
    else: #Caso a selecao do usuario seja diferente dos numeros indicados
        print('Selecao invalida')
        
             
print(Estoque)

firebase.patch('/pasta',Estoque)

