from movimentacoes import movimentacoes_estoque

def gerar_relatorio_movimentacoes(id_produto):
    movimentacoes = [m for m in movimentacoes_estoque if m.id_produto == id_produto]
    if movimentacoes:
        for mov in movimentacoes:
            print(f"Movimentação: {mov.movimentacao}, Quantidade: {mov.quantidade}, Data: {mov.data}")
    else:
        print("Nenhuma movimentação registrada para este produto.")


def consultar_historico_movimentacoes():
    if movimentacoes_estoque:
        for mov in movimentacoes_estoque:
            print(f"Produto ID: {mov.id_produto}, Tipo: {mov.movimentacao}, Quantidade: {mov.quantidade}, Data: {mov.data}")
    else:
        print("Nenhuma movimentação registrada no sistema.")