# Perguntar ao usuario qual é  nome dele
nome = input("Qual é o seu nome ? ")

# Remove espaço em branco da str
#nome = nome.strip()

# Deixa a primeira letra após o espaço maiuscula
#nome = nome.title()

# Remover espaço em branco da str e deixar em maiusculo
nome = nome.strip().title()

#dividir o nome do usuario do seu nome e sobre nome
fist, last = nome.split()

# Dizer olá ao usuario
print (f"Olá, {fist}!") 