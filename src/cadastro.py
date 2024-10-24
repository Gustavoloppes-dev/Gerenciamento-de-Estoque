from estruturaDeDados import Produto, Categoria

produtos = []
categorias = []

def cadastrar_produto(id, nome, categoria, quantidade, preco, fornecedor, setor):
    novo_produto = Produto(id, nome, categoria, quantidade, preco, fornecedor, setor)
    produtos.append(novo_produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def cadastrar_categoria(id, nome):
    nova_categoria = Categoria(id, nome)
    categorias.append(nova_categoria)
    print(f"Categoria '{nome}' cadastrada com sucesso!")

def consultar_produto(id):
    for produto in produtos:
        if produto.id == id:
            return produto
    print("Produto não encontrado.")
    return None
