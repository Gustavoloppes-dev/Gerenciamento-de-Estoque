from estruturaDeDados import MovimentacaoDeProdutos
from cadastro import consultar_produto

movimentacoes_estoque = []

def registrar_entrada(id_produto, quantidade):
    produto = consultar_produto(id_produto)
    if produto:
        produto.quantidade += quantidade
        movimentacao = MovimentacaoDeProdutos(id_produto, 'entrada', quantidade)
        movimentacoes_estoque.append(movimentacao)
        print(f"Entrada de {quantidade} unidades registrada para o produto '{produto.nome}'.")


def registrar_saida(id_produto, quantidade):
    produto = consultar_produto(id_produto)
    if produto:
        if produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            movimentacao = MovimentacaoDeProdutos(id_produto, 'saída', quantidade)
            movimentacoes_estoque.append(movimentacao)
            print(f"Saída de {quantidade} unidades registrada para o produto '{produto.nome}'.")
        else:
            print("Quantidade insuficiente no estoque.")