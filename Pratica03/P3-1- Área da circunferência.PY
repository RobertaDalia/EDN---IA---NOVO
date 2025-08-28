"""1- Área da circunferência

A fórmula para calcular a área de uma circunferência é: área = π X raio2. Considerando para
este problema que π = 3.14159265: 

• Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável
raio.
Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo
abaixo, com 4 casas após o ponto decimal.

"""
# Definimos o valor de PI conforme o enunciado
PI = 3.14159265

# Lemos o raio (um número com casa decimal). Ex.: 2.0
raio = float(input( "Insira o raio da circunferência:"))

# Calculamos a área da circunferência:
#    área = PI * raio2
area = PI * (raio ** 2)

# Imprimimos no formato pedido: "A=" + valor com 4 casas decimais.
print(f"A={area:.4f}")
