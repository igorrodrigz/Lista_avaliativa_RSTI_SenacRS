#A empresa de energia solar Energon necessita de um software capaz de
#calcular a área em metros onde serão instaladas as placas solares para
#produtores rurais. A empresa sempre fornecerá o comprimento e largura do
#terreno. Além disso todo o terreno fornecido será de área própria para a
#construção das placas.
print(20*"~~")
print("~~~~~~~CALCULADORA DE AREA ENERGON~~~~~~")
base = float(input("Insira os valores correspondentes á largura do terreno a ser calculado: "))
altura = float(input("Insira agora os valores correspondentes ao comprimento do terreno: "))
area = base * altura
print(f"A área total disponibilizada para instalação é de {area}m2")
