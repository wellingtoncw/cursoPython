#for c in range(0, 5):
#    print('Oi')

#for c in range(6, 0, -1): # contar decrescendo
 #   print(c)

#for c in range(0, 7, 2): # contar de 2 em 2
 #   print(c)

#num = int(input('Digite um número: '))
#for c in range(0, num+1):
#    print(c)
#print('FIM!')

#ini = int(input('Digite o inicio: '))
#fim = int(input('Digite fim: '))
#passo = int(input('Digite o passo: '))
#for c in range(ini, fim+1, passo):
 #   print(c)
#print('FIM!')

s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    #s = s + n
    s += n
print('O somatório dos valores é de {}.'.format(s))
