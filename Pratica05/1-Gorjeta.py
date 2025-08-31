"""Crie uma função que calcule a gorjeta a ser deixada em um restaurante,
 baseada no valor total da conta e na porcentagem de gorjeta desejada.
   Calcule o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: 
valor_conta (float): O valor total da conta
 porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna: 
float: O valor da gorjeta calculada"""

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
        float: O valor da gorjeta calculada.
    """
    return valor_conta * (porcentagem_gorjeta / 100)


# Entrada de dados
valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))

# Cálculo da gorjeta
valor_da_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)

# Saída final
print("\nResumo:")
print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Percentual da gorjeta: {porcentagem_gorjeta:.1f}%")
print(f"Valor da gorjeta: R$ {valor_da_gorjeta:.2f}")
print(f"Total a pagar (conta + gorjeta): R$ {valor_conta + valor_da_gorjeta:.2f}")

