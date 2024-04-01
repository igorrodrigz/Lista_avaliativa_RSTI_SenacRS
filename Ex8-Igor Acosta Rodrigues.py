


erro = "Erro, Dados incorretos"
erroSenhas = "Erro, as senhas não coincidem"

def cadastrar_usuario():
    print("=== Cadastro de Alunos ===")
    usuario = input("Digite seu nome de usuário: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    confirmar_senha = input("Confirme sua senha: ")

    if senha != confirmar_senha:
        print(erroSenhas)
        return cadastrar_usuario()

    return {'usuario': usuario, 'email': email, 'senha': senha}


def login(usuario_cadastrado):
    print("\n=== Login ===")
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    boasVindas = f"Bem vindo, {usuario} e tenha uma ótima semana!"
    if usuario_cadastrado is None:
        print(erro)
    elif usuario != usuario_cadastrado['usuario'] or senha != usuario_cadastrado['senha']:
        print(erro)
    else:
        print("Login efetuado com sucesso, boas aulas")
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
            usuario_cadastrado = cadastrar_usuario()
        elif opcao == 'l':
            login(usuario_cadastrado)
        elif opcao == 's':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha 'c' para cadastrar, 'l' para login ou 's' para sair.")

main()

