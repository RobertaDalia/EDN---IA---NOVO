"""Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres
 e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida
   ou o usuário digite 'sair'."""

def verificar_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == "sair":
            print("Programa encerrado.")
            break

        # Verifica se a senha tem pelo menos 8 caracteres
        comprimento_valido = len(senha) >= 8

        # Verifica se contém pelo menos um número
        contem_numero = any(char.isdigit() for char in senha)

        if comprimento_valido and contem_numero:
            print("✅ Senha forte cadastrada com sucesso!")
            break
        else:
            print("⚠️ Senha fraca! A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.\n")

# Executa o programa
verificar_senha()
