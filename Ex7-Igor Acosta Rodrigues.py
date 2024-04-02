#Desenvolva um programa que permita ao usuário solicitar várias vezes a
#geração de um número aleatório de 1 a 20. Retorne uma informação ao usuário
#baseado na tabela abaixo. Para finalizar o programa o usuário precisa digitar
#-1. Adicionalmente o usuário pode informar um "modificador" para o número,
#ou seja, é possível ter um valor acrescentado a geração. Por exemplo, digita-se
#+5 no prompt, então acrescenta-se +5 ao valor que será sorteado nas próximas
#gerações de número.


import random
from time import sleep

# Gerando o numero aleatorio de (1 a 20)
NumeroAleatorio = random.randint(1, 20)

# Boas Vindas
print(20*"~~")
print("Bem-Vindo ao Dado de 20 Lados 2.0, Boa Sorte Aventureiro  !")
print("Jogando...!")
sleep(1)
print(20*"~~")

#Selecionador de frases
if NumeroAleatorio == 1 :
    print("Erro Crítico!!")
elif NumeroAleatorio == 20 :
    print("Acerto Crítico !!!")
else:
    print(f"O Numero sorteado foi {NumeroAleatorio}!")

print(20*"~~")


#Soma o modificador + Aleatorio
while True:
    try:
        modificador = int(input("""
Deseja adicionar um Modificador para o número sorteado?
[sair] Digite -1 para encerrar o programa
[Jogar novamente] Digite o número que deseja acrescentar ao sorteio: """))

        if modificador == -1:
            print("Encerrando o programa. Obrigado por jogar!")
            break
        else:
            # Gerando um novo numero de (1 a 20)
            NumeroAleatorioNovo = random.randint(1, 20)
            NumeroAleatorioNovoModificado = NumeroAleatorioNovo + modificador
            print(f"O número sorteado {NumeroAleatorioNovo}, com o modificador, é {NumeroAleatorioNovoModificado}!")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou -1 para sair.")

