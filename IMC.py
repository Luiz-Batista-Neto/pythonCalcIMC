print("Programa para calcular IMC")
# O IMC é reconhecido como padrão internacional para avaliar o grau de sobrepeso e obesidade. 
# É calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).

nome = str(input("Olá, bem vindo ao teste de IMC, qual é o seu nome?: "))
idade = int(input(f"Ok {nome}, agora nos informe a sua idade: "))

peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

IMC = float(peso / (altura * altura))

def ExibirMsgFinal():
    print(f'Oi {nome}, você possui {idade} anos de idade, Seu IMC é... {IMC:.2f}')

if IMC <= 16:
    ExibirMsgFinal()
    print("Menor que 16 - Magreza grave, procure um nutricionista e pega uns quilinhos =p")
elif IMC <= 17:
    ExibirMsgFinal()
    print("Entre 16 a 17 - Magreza moderada, procure um nutricionista e pega uns quilinhos =p")
elif IMC <= 18.5:
    ExibirMsgFinal()
    print("17 a menor que 18,5 - Magreza leve")
elif IMC <= 25:
    ExibirMsgFinal()
    print("18,5 a menor que 25 - Saudável, Parabéns! continue assim")
