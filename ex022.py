var1 = float(input('Digite a largura desejada em metros. Separe os decimais por pontos  '))
var2 = float(input('Digite a altura desejada. Siga as mesmas regras da largura  '))
var3 = var1*var2
var4 = var3/2
print('A largura digitada foi {}m. e a altura foi {}m. Sua área total é {:.2f}m.\n Para pintar essa aérea seriam precisos {:.2f}L. de tinta.'.format(var1, var2, var3, var4))
