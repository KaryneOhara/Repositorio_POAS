#pip install requests
import requests

URL = "http://127.0.0.1:8000"

def listar_livros():
    r = requests.get(f"{URL}/livros")
    if r.status_code == 200:
        print(r.text)
def cadastrar_livros():
    titulo = input("Digite o título: ")
    ano = int(input("Digite o ano: "))
    edicao = int(input("Digite a edicao: "))
    livro = {
        "titulo":titulo,
        "ano":ano,
        "edicao":edicao
    }
    r = requests.post(f"{URL}/livros", json=livro)
def listar_livro(titulo):
    r = requests.get(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print(r.text)

def excluir_livros(titulo):
    r = requests.delete(f"{URL}/livros/{titulo}")
    if r.status_code == 200:
        print("Excluído com sucesso")
    else:
        print(r.text)

def editar_livro(titulo):
    r = requests.put(f"{URL}/livros/{titulo}", json=novos_dados)

    nova_edicao = input("Digite a nova edição: ")
    novo_ano = int(input("Digite o novo ano: "))
    novos_dados = {
        "titulo": titulo,
        "ano": novo_ano,
        "edicao": nova_edicao
    }

    if r.status_code == 200:
        print('Livro atualizado com sucesso:', r.text)
    else:
        print('Erro ao atualizar livro:', r.text)

def menu():
    print ("1 - Listar livros")
    print ("2 - Listar livros peto título")
    print ("3 - Cadastrar livro")
    print ("4 - Deletar livro")
    print ("5 - Editar livro")
    print ("6 - Sair")
    return int(input("Digite sua opção: "))

opcao = menu()
while opcao != 6:
    if opcao == 1:
        listar_livros()
    elif opcao == 2:
        titulo = input("Digite o título: ")
        listar_livro(titulo)
    elif opcao == 3:
        cadastrar_livros()
    elif opcao == 4:
        titulo = input("Digite o título: ")
        excluir_livros(titulo)
    elif opcao == 5:
        titulo = input("Digite o título: ")
        editar_livro(titulo)
    opcao=menu()
