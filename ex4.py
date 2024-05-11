def e_palindromo(texto):

    texto = texto.replace(" ", "").lower()
    

    return texto == texto[::-1]





def main():
    string = "socorram me subi no onibus em marrocos"


    if e_palindromo(string):
        print("A string é um palíndromo.")
    else:
        print("A string não é um palíndromo.")