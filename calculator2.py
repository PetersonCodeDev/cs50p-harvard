def main():
    x = int(input("Qual é o seu valor que quer saber ao quadrado?:"))
    print ("seu valor ao quadrado é ", quadrado(x))


def quadrado(n):
    return pow(n, 2)


main()