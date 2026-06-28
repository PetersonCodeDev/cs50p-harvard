x = float(input("Qual é o seu primeiro numero: ")) #float aceita numeros decimais, não só inteiros
y = float(input("Qual é o seu segundo numero: "))

z = round (x / y, 2) #arredonda para 2 casas decimais

print(f"{z:.2f}") #formata o numero com 2 casas decimais