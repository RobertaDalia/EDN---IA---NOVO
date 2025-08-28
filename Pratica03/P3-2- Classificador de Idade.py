"""2- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais)."""

# Pedimos a idade do usuário.
# input() lê como texto, então usamos int(...) para converter para número inteiro.
idade = int(input("Insira sua idade:"))

# Agora usamos if/elif/else para verificar em qual faixa a idade se encaixa.
if idade >= 0 and idade <= 12:
    print("Criança")
elif idade >= 13 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade inválida")

