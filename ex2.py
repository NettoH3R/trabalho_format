import string

def contar_palavras(texto):

    texto_sem_pontuacao = texto.translate(str.maketrans('', '', string.punctuation))

    palavras = texto_sem_pontuacao.split()
    
    return len(palavras)



def main():
    
    texto = "Olá! Este é um exemplo de texto. Será que conseguimos contar o número de palavras corretamente?"

    print("Número de palavras no texto:", contar_palavras(texto))