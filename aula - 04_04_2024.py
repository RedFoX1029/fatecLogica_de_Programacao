'''
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = (n1 + n2) / 2
if (n1 > 10 or n1 < 0) or (n2 > 10 or n2 < 0):
    print("Valor incorreto!!!!")
else:
    print("A média é: ", n3)

    if n3>=6:
        print("Passou")
    elif n3 < 6:
        print("Reprovou")
        n4 = float(input("Digite a sua nota de recuperação: "))
        if (n4 + n1 + n2) / 3 >= 6:
            print("Aprovado!!!")
        else:
            print("Reprovado mesmo assim")
'''

'''
s = str(input("Digite M ou F: "))

if s == 'm':
    print("Masculino")
elif s == 'f':
    print("Feminino")    
else:
    print("Digito incorreto")
'''

'''
a = float(input("Digite a altura: "))
p = float(input("Digite o peso: "))

imc = p / (a ** 2)

if imc <= 25 and imc >= 18:
    print("Peso normal: ", imc)
elif imc <= 30 and imc > 25:
    print("Sobrepeso: ", imc)
elif imc <= 40 and imc > 30:
    print("Obesidade moderada: ", imc)
elif imc > 40:
    print("Obesidade mórbida: ", imc)
'''

'''
h = int(input("Digite a quantidade de horas: "))
m = int(input("Digite a quantidade de minutos: "))

minutos = (h * 60) + m

print("Os minutos totais são: ", minutos)
'''

'''
C = float(input("Digite a temperatura em C°: "))

F = 32 + 1.8 + C

print("C°:", C, "-- F°:", F)
'''

'''
s = float(input("Digite o antigo salario: "))
a = float(input("Digite o aumento: "))

salarioplus = ((s / 100) * a) + s

print("O novo salario é:", salarioplus)
'''

'''
vet = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Novembro", "Dezembro"]
for X in range (0, 12, +1):
    valorvenda = str(input("Digite o numero de vendas de",vet[0], ":" ))
'''

'''
cotacao = float(input("Digite a cotação de dolar atual: "))
dolar = float(input("Digite o valor em dolar: "))

reais = dolar * cotacao

print("US:", dolar, "-- R$:", reais)


dia = int(input("Digite o valor do dia(de 1 á 7): "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sábado")
    case _:
        print("Valor incorreto")
'''

'''
N = int(input("Digite o primeiro numero: "))
print(N**2)
'''

'''
KM = float(input("Digite a quantidade de quilometros rodados: "))
L = float(input("Digite o consumo de combustivel: "))

KM_L = KM / L

print(KM_L)

if KM_L <= 8:
    print("Consumo normal")
else:
    print("Consumindo muito combustivel")
'''

m = int(input("Digite o dia do mes: "))

if(m == 1):
    print("Janeiro")
elif(m == 2):
    print("Fevereiro")
elif(m == 3):
    print("Março")
elif(m == 4):
    print("Abril")
elif(m == 5):
    print("Maio")
elif(m == 6):
    print("Junho")
elif(m == 7):
    print("Julho")
elif(m == 8):
    print("Agosto")
elif(m == 9):
    print("Setembro")
elif(m == 10):
    print("Outubro")
elif(m == 11):
    print("Novembro")
elif(m == 12):
    print("Dezembro")
else:
    print("Numero incorreto!!")
