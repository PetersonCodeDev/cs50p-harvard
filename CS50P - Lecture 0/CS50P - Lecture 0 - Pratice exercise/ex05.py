valor = float(input("Digite o valor em reais: "))
cotação = float(input("Digite a cotação do dólar: "))
dólares = valor / cotação
print(f"Com R$ {valor} você pode comprar US$ {dólares:.2f}")