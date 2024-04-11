'''
N = int(input("Digite o primeiro numero: "))
print(N**2)
'''
'''
tamanho = int(input("Digite a quantidade de vezes que deseja saber a taxa de consumo: "))
for X in range(0, tamanho, +1):
    KM = float(input("Digite a quantidade de quilometros rodados: "))
    L = float(input("Digite o consumo de combustivel: "))

    KM_L = KM / L

    print(KM_L)

    if KM_L <= 8:
        print("Consumo normal")
    else:
        print("Consumindo muito combustivel")
'''