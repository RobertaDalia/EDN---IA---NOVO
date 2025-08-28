""" 3- Calculadora de Média Escolar 

Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
Nota 1: 7.5

Nota 2: 8.0

Nota 3: 6.5 
O programa deve calcular a média e exibir todas as notas e o resultado final,
 arredondando para duas casas decimais.
"""
# Definindo as notas do aluno
Nota1 = 7.5
Nota2 = 8.0
Nota3 = 6.5 

# Calculando a média
media = (Nota1 + Nota2 + Nota3)/3

# Exibindo os resultados
print("Notas dos alunos:")
print(f"Nota do aluno 01: {Nota1:.2f}")
print(f"Nota do aluno 02: {Nota2:.2f}")
print(f"Nota do aluno 03: {Nota3:.2f}")
print(f"A média geral dos alunos foi de : {media:.2f}.")