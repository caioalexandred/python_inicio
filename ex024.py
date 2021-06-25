var1 = float(input('Digite o valor do salário. Separe os centavos por ponto   '))
var2 = var1*0.15
var3 = var1+var2
print('O salário referido foi de R$ {:.2f}. Com o novo aumento fica R$ {:.2f}.'.format(var1,var3))
