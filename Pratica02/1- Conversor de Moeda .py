"""1- Conversor de Moeda 

Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

Valor em reais: R$ 100.00

Taxa do dólar: R$ 5.60

Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

# Definindo os valores conhecidos
valor_reais = 100.00   # Valor em reais a ser convertido
taxa_dolar = 5.60      # Cotação do dólar em reais
taxa_euro = 6.60       # Cotação do euro em reais

# Conversão de reais para dólares
valor_dolares = valor_reais / taxa_dolar

# Conversão de reais para euros
valor_euros = valor_reais / taxa_euro

# Exibindo os resultados com duas casas decimais
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor em dólares: US$ {valor_dolares:.2f}")
print(f"Valor em euros: € {valor_euros:.2f}")