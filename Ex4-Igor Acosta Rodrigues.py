#Desenvolva um programa que peça a bandeira atual de energia elétrica e o
#valor gasto em Watts. As bandeiras são, Verde (R$ 1 por watt consumido),
#Amarela (R$ 3 por Watt consumido) e Vermelha (R$ 7 por Watt consumido).
#Retorne ao usuário o valor da sua conta de luz.

#Selecione a bandeira
Bandeira = int(input("""Informe ao programa sua bandeira atual: 
    [1] Verde
    [2] Amarela
    [3] Vermelha
    """))

WattsConsumido = float(input("Informe o valor consumido em Watts: "))

#CalculoWatts = Bandeira * WattsConsumido

if Bandeira == 1 :
    CalculoWatts = 1 * WattsConsumido
elif Bandeira == 2 :
    CalculoWatts = 3 * WattsConsumido
elif Bandeira == 3 :
    CalculoWatts = 7 * WattsConsumido
else :
    print("Valor inválido, por favor informe a sua bandeira novamente")
print(f"O valor da sua conta de energia atual é de R${CalculoWatts}0")