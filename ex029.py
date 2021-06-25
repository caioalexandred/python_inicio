var1 = int(input('Quantos dias ficou-se com o carro?   '))
var2 = float(input('Quantos Km foram percorridos?   '))
var3 = float(60)
var4 = float(0.15)
var5 = (var1*var3)+ (var2*var4)
print('Tendo o sr. ficado {} dias com o carro e percorrido {} Km o total a pagar é R${:.2f}.\n Nossos preços hoje são de '
      'R${} o dia e R${} por Km rodado'.format(var1, var2, var5, var3, var4))

