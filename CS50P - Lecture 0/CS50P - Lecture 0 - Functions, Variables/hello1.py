# Perguntar ao usuario qual é  name dele
name = input("Qual é o seu name ? ")

# Remove espaço em branco da str
#name = name.strip()

# Deixa a primeira letra após o espaço maiuscula
#name = name.title()

# Remover espaço em branco da str e deixar em maiusculo
name = name.strip().title()

#dividir o name do usuario do seu name e sobre name
first, last = name.split()

# Dizer olá ao usuario
print (f"Olá, {first}!") 