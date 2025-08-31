"""Crie uma função que verifique se uma palavra ou frase é um palíndromo
 (lê-se igual de trás para frente, ignorando espaços e pontuação). 
 Se o resultado é True, responda “Sim”, se o resultado for False, 
 responda “Não”."""

def palindromo(frase):
    # Remove espaços e converte para minúsculas
    texto_limpo = ''.join(char.lower()
                          for char in frase 
                          if char.isalnum()
                          )
    return texto_limpo == texto_limpo[::-1] # comparando o texto limpo a sua versão invertida

texto = input("Digite a expressão ou palavra: ")
resultado =  palindromo(texto)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{texto}' é um palíndromo? {resposta}")