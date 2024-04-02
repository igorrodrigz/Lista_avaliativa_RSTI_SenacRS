# Desenvolva um programa que solicite cadastramento do usuário. Os dados a
# serem cadastrados são: nome de usuário, email, senha e confirmação de
# senha. Feito o cadastro peça ao mesmo para se logar no sistema, verifique
# possíveis erros nos formulários como nos campos confirmar senha, usuário,
# senha e email.

from time import sleep

erro = "Erro, dados incorretos"
erroSenhas = "Erro, as senhas não coincidem!"


def cadastrar_aluno():
    print(8*"~~","Cadastro de Alunos",8*"~~")
    sleep(1)
    usuario = input("Digite seu nome de usuário: ")
    email = input("Digite seu melhor email: ")
    senha = input("Digite sua senha: ")
    confirmar_senha = input("Confirme sua senha: ")

    if senha != confirmar_senha:
        print(erroSenhas)
        return cadastrar_aluno()

    return {'usuario': usuario, 'email': email, 'senha': senha}

def login(usuario_cadastrado):
    print("\n======= Login ========")
    sleep(1)
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    boasVindas = f"Bem vindo, {usuario} e tenha uma ótima semana!"
    if usuario_cadastrado is None:
        print(erro)
    elif usuario != usuario_cadastrado['usuario'] or senha != usuario_cadastrado['senha']:
        print(erro)
    else:
        print("Login efetuado com sucesso, boas aulas.")
        sleep(1)
        print(boasVindas)

def main():
    usuario_cadastrado = None

    while True:
        opcao = input("""
        Bem vindo a Central do Aluno RSTI:
        por favor, digite a opção desejada
        [c] Cadastro
        [l] Login
        [s] Sair
        """)

        if opcao == 'c':
            usuario_cadastrado = cadastrar_aluno()
        elif opcao == 'l':
            login(usuario_cadastrado)
        elif opcao == 's':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, entre 'c' para cadastrar, 'l' para login ou 's' para sair.")

main()
