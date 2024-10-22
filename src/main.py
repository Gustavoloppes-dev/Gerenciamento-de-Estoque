from cadastro import cadastrarProduto, cadastrarCategoria, consultar_produto
from movimentacoes import registrar_entrada, registrar_saida
from relatorios import gerar_relatorio_movimentacoes, consultar_historico_movimentacoes

cadastrarCategoria(1, "Eletrônicos")
cadastrarCategoria(2, "Alimentos")


cadastrarProduto(1, "Smartphone", "Eletrônicos", 50, 1200.00, "Fornecedor X")
cadastrarProduto(2, "Câmera", "Eletrônicos", 20, 800.00, "Fornecedor Y")


registrar_entrada(1, 10)  
registrar_saida(2, 5)     

produto = consultar_produto(1)
if produto:
    print(f"Produto consultado: {produto.nome}, Estoque: {produto.quantidade}")


gerar_relatorio_movimentacoes(1)


consultar_historico_movimentacoes()