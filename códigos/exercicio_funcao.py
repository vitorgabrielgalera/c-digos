def dados(nome,idade,altura):
    print(f"""nome: {nome}
idade: {idade}
altura: {altura}""")
    
nome = input("digite o nome: ")
idade = input("digite a idade: ")
altura = input("digite a altura: ")

dados(nome,idade,altura)









def consumo(carro,litros_por_km,km_rodados):
    litros_por_km = float(litros_por_km)
    km_rodados = float(km_rodados)
    km_por_l = km_rodados/litros_por_km
    print(f"""carro: {carro}
litros por km: {litros_por_km}
km rodados: {km_rodados}
km por litro: {km_por_l}""")
    
carro = input("digite o carro: ")
litros_por_km = input("digite o consumo de litros de gasolina: ")
km_rodados = input("digite os km rodados: ")

consumo(carro,litros_por_km,km_rodados)









def custo_total(carro,litros_por_km,km_rodados,gasolina):
    gasolina = float(gasolina)
    litros_por_km = float(litros_por_km)
    km_rodados = float(km_rodados)
    gasto = km_rodados/litros_por_km*gasolina
    print(f"""carro: {carro}
litros por km: {litros_por_km}
km rodados: {km_rodados}
custo total: {gasto}""")
    
carro = input("digite o carro: ")
litros_por_km = input("digite o consumo de litros de gasolina: ")
km_rodados = input("digite os km rodados: ")
gasolina = input("digite o valor da gasolina: ")

custo_total(carro,litros_por_km,km_rodados,gasolina)