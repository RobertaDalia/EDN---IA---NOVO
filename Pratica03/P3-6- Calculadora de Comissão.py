"""6- Calculadora de Comissão

Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido."""

# Entrada de dados
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o total de vendas: "))

# Cálculo da comissão (15% das vendas)
comissao = vendas * 0.15

# Total a receber
total = salario_fixo + comissao

# Saída formatada
print(f"TOTAL A RECEBER = R$ {total:.2f}, onde R${salario_fixo:.2f} foi de salário e R${comissao:.2f} de comissão.")