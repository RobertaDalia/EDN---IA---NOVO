"""5- Calculadora de Número Inteiro
 Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença 
 do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras internas.
"""

A = int(input("Digite um número inteiro:"))
B = int(input("Digite outro número inteiro:"))
C = int(input("Digite mais um número inteiro:"))
D = int(input("Digite o ultimo número inteiro:"))

DIFERENCA = (A * B - C * D)

print("Você digitou quatro números inteiros, a seguir te mostrarei o resultado da diferença " \
"do produto de A e B pelo produto de C e D segundo a fórmula: A * B - C * D. ")
print(f"DIFERENCA = {DIFERENCA}")