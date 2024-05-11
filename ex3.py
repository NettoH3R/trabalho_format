def encontrar_ocorrencias(texto, palavra):

    texto = texto.lower()
    palavra = palavra.lower()
    

    ocorrencias = []
    

    indice = 0
    

    while True:

        indice = texto.find(palavra, indice)
        

        if indice == -1:
            break
        

        ocorrencias.append(indice)
        

        indice += 1
    

    return ocorrencias




def main():

    texto = "Python é uma linguagem de programação muito poderosa. Python é usada em várias aplicações."
    palavra = "Python"


    print("Ocorrências da palavra no texto:", encontrar_ocorrencias(texto, palavra))