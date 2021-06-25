var = float(input('Digite uma quantidade de dinheiro: R$ '))
var1 = var/5
print('O valor digitado foi {}. Com esse valor você pode comprar US${:.2f} dólar(es).(dólar cotado a R$5)'.format(var, var1))
