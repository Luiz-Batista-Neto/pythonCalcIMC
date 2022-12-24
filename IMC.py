print("Programa para calcular IMC")
# O IMC é reconhecido como padrão internacional para avaliar o grau de sobrepeso e obesidade. 
# É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).

peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))
IMC = peso / (altura * altura)
print(f'Seu IMC é... {IMC:.2f}')