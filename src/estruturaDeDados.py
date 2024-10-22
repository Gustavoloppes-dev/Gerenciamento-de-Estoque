class Produto :
    def __init__(self,id, nome, categoria, quantidade, preco, fornecedor):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.fornecedor = fornecedor

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class MovimentacaoDeProdutos:
    def __init__(self, id_produto, movimentacao, quantidade, data=None):
        self.id_produto = id_produto   
        self.movimentacao = movimentacao               
        self.quantidade = quantidade
        self.data = data