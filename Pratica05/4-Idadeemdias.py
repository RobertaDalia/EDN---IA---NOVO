"""Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento."""

from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade de uma pessoa em dias com base no ano de nascimento.

    Args:
        ano_nascimento (int): O ano em que a pessoa nasceu.

    Returns:
        int: A idade da pessoa em dias.
    """
    # Obtém a data atual
    data_atual = date.today()
    
    # Calcula o ano atual
    ano_atual = data_atual.year
    
    # Calcula a idade aproximada em anos
    idade_em_anos = ano_atual - ano_nascimento
    
    # Calcula a idade em dias, considerando 365 dias por ano
    idade_em_dias = idade_em_anos * 365
    
    return idade_em_dias

# Solicitando o ano de nascimento ao usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade_dias = calcular_idade_em_dias(ano_nascimento)
print(f"Uma pessoa que nasceu em {ano_nascimento} tem aproximadamente {idade_dias} dias de vida.")