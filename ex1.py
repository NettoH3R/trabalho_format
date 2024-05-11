entrada = input("Digite uma sequência de números inteiros separados por espaços: ")



numeros = entrada.split()

numeros_inteiros = [int(numero) for numero in numeros]

media = sum(numeros_inteiros) / len(numeros_inteiros)



print("A média dos números é:", media)