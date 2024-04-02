#Desenvolva um pequeno programa que peça a base e o expoente, calcule o
#resultado da potência e mostre ao usuário.
import math
# Valores
print("Bem-vindo à calculadora de potenciação, para dar continuidade insira os \nvalores solicitados á baixo...\n")
x = float(input("Insira o valor de base a ser calculado: "))
y = float(input("Insira o valor do expoente a ser calculado: "))

#Calculo
calculo = math.pow(x, y)
print(calculo)