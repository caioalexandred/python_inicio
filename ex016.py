#operadores aritméticos
v1 = int(input('Digite o total de casos  '))
v2 = int(input('digite o total de mortes  '))
v3 = int(100)
v4 = int(210000000)
re1 = v2/v1*v3
re2 = v2/v4*v3
print('O total de casos foi {}, de mortes foi {} '.format(v1, v2))
print('Poporcionalmente o número de mortes é de {:.2f}%, e em relação à população é de {:.2f}%'.format(re1, re2))

#print('O valor digitado foi', v1)
#print('vinte por cento de ', v1, 'é ', re1)

