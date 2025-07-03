from fastapi import FastAPI,HTTPException
from models import Livro
from typing import List
app = FastAPI()
livros:List[Livro]=[]

@app.get("/livros",response_model=List[Livro])
def listar_livros():
    return livros

@app.get("/livros/{titulo}",response_model=Livro)
def listar_livros( titulo:str):
    for livro in livros:
        if livro.titulo == titulo:
            return livro
    raise HTTPException(404,"Não localizado")

@app.delete("/livros/{titulo}",response_model=Livro)
def deletar_livro(titulo:str):
    for id, livro in enumerate(livros):
        if livro.titulo == titulo:
            livros.pop(id)
            return livro
    raise HTTPException(404,"Não localizado")

@app.post("/livros", response_model=Livro)
def criar_livro(livro:Livro):
    livros.append(livro)
    return livro
    raise HTTPException(404,"Não localizado")

@app.put("/livros/{titulo}",response_model=Livro)
def editar_livro(titulo:str, novos_dados: Livro):
    for id, livro in enumerate(livros):
        if livro.titulo == titulo:
            livros[id] = novos_dados
            return novos_dados
    raise HTTPException(404,"Não localizado")


# 1 - Listar todos os livros
# 2 -  Pesquisa livro por título: peça ao usuário o título para pesquisa
# 3 - Cadastrar um livro: peça ao usuário os dados do livros e envie o json para cadastrar
# 4 - Deletar um livro:: peça ao usuário o título para deletar
# 5 - Editar um livro: faça a busca pelo livro e edite os dados dele: Implementa a rota da API e a funcionalidade via requests
# 6 - Sair