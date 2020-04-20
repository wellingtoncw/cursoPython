#nome = input('Qual é seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1 ** n2
print('A soma vale {}, o produto vale {}, a divisão vale {:.3f}!'.format(s, m, d), end=' ')
print('Divisão Inteiro {}, Exponenciação {}!'.format(di, e))



