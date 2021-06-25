var1 = float(input('Qual o preço do produto? (separe os centavos por ponto)   '))
var2 = var1*0.05
var3 = var1-var2
print('O produto custa R$ {:.2f} e com o nosso incrível desconto vai para R$ {:.2f}'.format(var1, var3))
