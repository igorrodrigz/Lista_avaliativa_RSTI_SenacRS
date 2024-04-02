print("Bem vindo ao Calculador de Terrenos 4.0 da Energon")
print(20 * "~~")

def calcularArea(comprimento, largura, *areas_menores):
    area_total = comprimento * largura
    for area in areas_menores:
        area_total += area
    return area_total

def excluir(areas_menores):
    if areas_menores:
        indice = int(input("Digite o índice do terreno que deseja excluir: "))
        if 0 <= indice < len(areas_menores):
            del areas_menores[indice]
            print("Terrenos menores removidos com sucesso.")
            return calcularArea()
        else:
            print("Índice inválido. Nenhum terreno foi removido.")
    else:
        print("Não há mais terrenos para excluir.")

def main():
    comprimento_terreno = float(input("Digite o comprimento do terreno em metros: "))
    largura_terreno = float(input("Digite a largura do terreno em metros: "))

    areas_menores = []
    while input("""
    Deseja adicionar uma área menor?
    [s] para Sim
    [n] para Não
    """) == "s":
        areas_menores.append(float(input("Digite a área menor a ser adicionada em metros quadrados: ")))
    global areaFinal
    areaFinal = calcularArea(comprimento_terreno, largura_terreno, *areas_menores)
    print(f"A área total para instalação das placas solares é de {areaFinal} metros quadrados.")

    if areas_menores and input("""
    Deseja excluir alguma área menor?
    [s] para Sim
    [n] para Não
    """) == "s":
        excluir(areas_menores)
        #print(areaFinal)


if __name__ == '__main__':
    main()
