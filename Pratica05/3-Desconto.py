"""Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo 
do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada:
 preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10)."""

# Requisitos:
# 1. Permitir que o usuário informe o preço do produto e o percentual de desconto.
# 2. Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
# 3. Exibir o preço final com duas casas decimais para garantir precisão.

def calcular_desconto(preco_original, percentual_desconto):
    """
    Calcula o preço final de um produto após a aplicação de um desconto.

    Args:
        preco_original (float): O preço inicial do produto.
        percentual_desconto (float): O percentual de desconto a ser aplicado.

    Returns:
        float: O preço final do produto com o desconto aplicado.
    """


    # Converter o percentual para um valor decimal
    valor_desconto = preco_original * (percentual_desconto / 100)
    
    # Calcular o preço final
    preco_final = preco_original - valor_desconto
    
    return preco_final

# Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
try:
    # Solicitar as entradas do usuário
    preco_do_produto = float(input("Digite o preço do produto: "))
    percentual_do_desconto = float(input("Digite o percentual de desconto: "))

    # Chamar a função para calcular o preço final
    preco_final_do_produto = calcular_desconto(preco_do_produto, percentual_do_desconto)

    # Exibir o preço final com duas casas decimais
    print(f"O preço final com desconto é: R$ {preco_final_do_produto:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")
