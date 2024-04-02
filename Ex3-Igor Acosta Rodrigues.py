#Desenvolva um pequeno programa que gere um número aleatório entre 1 e 3.
#Se o valor for 1 escreva "Não foi dessa vez". Se o valor for 2 escreva "Nossa foi
#quase!". Se o valor for 3 escreva "Passou raspando!!!"
import random
from time import sleep
# Gerador de numero aleatorio
NumeroAleatorio = random.randint(1,3)

print(f"O numero sorteado foi {NumeroAleatorio}:")

print("Analisando...")
sleep(1)

# Seleção de frases
if NumeroAleatorio == 1 :
    print("Não foi dessa vez")
elif NumeroAleatorio == 2 :
    print("Nossa foi quase!")
else :
    print("Passou raspando!!!")