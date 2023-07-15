print('{:=^80}'.format(' Gerenciamento de salário '))


salario = float(input('Informe o seu salário desse mês: '))
investimento = salario * 0.10
despesas = salario * 0.60
estudos_e_outros = salario * 0.30


print('Com o seu salário desse mês, você deve gastar:')
print('')
print(f'Com despesas de moradia, conta de luz, Internet e alimentação: R$ {despesas:.2f}')
print('')
print(f'Com seu investimento, você deve gastar: R$ {investimento:.2f}')
print('')
print(f'Com estudos e outros gastos, você deve gastar: R$ {estudos_e_outros:.2f}')
