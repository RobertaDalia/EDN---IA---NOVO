""" 2- Calculadora de Desconto 

Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:



Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

# Definindo as informações do produto
nome_produto = "Camiseta"   # Nome do produto
preco_original = 50.00      # Preço sem desconto
porcentagem_desconto = 20   # Porcentagem de desconto (%)

# Calculando o valor do desconto
valor_desconto = preco_original * (porcentagem_desconto / 100)

# Calculando o preço final após aplicar o desconto
preco_final = preco_original - valor_desconto

# Exibindo os resultados
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: -R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
