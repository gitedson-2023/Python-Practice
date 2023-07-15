print('{:=^40}'.format(' SORVETERIA '))
print('')
print('{:^40}'.format(' SABORES '))
print('Chocolate --------------------> R$ 15,00')
print('Morango   --------------------> R$ 10,00')
print('')


preco_choco = 15
sabor = int(input('Escolha o sabor do sorvete [digite 1 para chocolate e 2 para morango]: '))
bolas = int(input('Quantas bolas de sorvete? '))

if sabor == 1 and bolas > 3:
    print(f'Você terá 10% de desconto. O preço final será de R${preco_choco - (preco_choco*0.10):.2f}')
elif sabor == 1 and bolas <= 3:
    print(f'Você terá 5% de desconto. O preço final será de R${preco_choco - (preco_choco*0.05):.2f}')
elif sabor == 2:
    print('Sorvete sem desconto. Você pagará R$ 10,00')