distancia = int(input("Digite a distancia em KM: "))
consumo = float(input("Qual o consumo medio do veiculo em km "))
preco_combustivel = float(input("Qual o preço do combustivel?: "))

total_viagem = (distancia / consumo) * preco_combustivel

print("o custo estimado é de: ", total_viagem)