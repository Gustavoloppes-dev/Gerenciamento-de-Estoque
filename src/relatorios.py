from movimentacoes import movimentacoes_estoque
from cadastro import produtos

estoque_minimo = 15
estoque_maximo = 60

def gerar_relatorio_movimentacoes(id_produto):
    movimentacoes = [movimentacao for movimentacao in movimentacoes_estoque if movimentacao.id_produto == id_produto]
    if movimentacoes:
        for movimentacao in movimentacoes:
            print(f"Movimentação: {movimentacao.movimentacao}, Quantidade: {movimentacao.quantidade}")
    else:
        print("Nenhuma movimentação registrada para este produto.")


def consultar_historico_movimentacoes():
    if movimentacoes_estoque:
        for movimentacao in movimentacoes_estoque:
            print(f"Produto ID: {movimentacao.id_produto}, Tipo: {movimentacao.movimentacao}, Quantidade: {movimentacao.quantidade}")
    else:
        print("Nenhuma movimentação registrada no sistema.")

def gerar_relatorio_estoque_limite():
    estoque_baixo = [produto for produto in produtos if produto.quantidade <= estoque_minimo]
    excesso_estoque = [produto for produto in produtos if produto.quantidade >= estoque_maximo]

    print("\n--- Relatório de Produtos com Estoque Baixo ---")
    if estoque_baixo:
        for produto in estoque_baixo:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}, Localização: {produto.setor}")
    else:
        print("Nenhum produto com estoque baixo.")

    print("\n--- Relatório de Produtos com Excesso de Estoque ---")
    if excesso_estoque:
        for produto in excesso_estoque:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}, Localização: {produto.setor}")
    else:
        print("Nenhum produto com excesso de estoque.")