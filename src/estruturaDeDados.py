class Produto :
    def __init__(self,id, nome, categoria, quantidade, preco, fornecedor, setor):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.fornecedor = fornecedor
        self.setor = setor

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Movimentacao_De_Produtos:
    def __init__(self, id_produto, movimentacao, quantidade):
        self.id_produto = id_produto   
        self.movimentacao = movimentacao               
        self.quantidade = quantidade
        