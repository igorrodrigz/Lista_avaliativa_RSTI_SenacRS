def soma (a, b):
    return a + b

def subtracao(a, b):
    return a - b

def main():
    opcao = 1
    while opcao:
        print("""
        Menu de Operações:
        [1] Somar
        [2] Subtrair
        [0] Sair
        """)

        opcao = int(input("Escolha uma operação: "))

        if opcao in (1, 2):
            num1 = float(input("Digite o valor do primeiro número: "))
            num2 = float(input("Digite o valor do segundo número: "))

            if opcao == 1:
                resultado = soma(num1, num2)
                print(f"soma: {resultado}")
            else:
                resultado = subtracao(num1, num2)
                print(f"Subtração: {resultado}")

            while True:
                mais_numeros = input("Deseja adicionar mais numeros? [s] Sim ou [n] Não")
                if mais_numeros == "s":
                    novo_numero = float(input("Digite o Próximo numero: "))
                    if opcao == 1:
                        resultado = soma(resultado, novo_numero)
                    else:
                        resultado = subtracao(resultado, novo_numero)
                elif mais_numeros == "n":
                    break
                else:
                    print("Resposta inválida. Digite [s] para adicionar ou [n] para sair")
        elif opcao == 0:
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente")

main()