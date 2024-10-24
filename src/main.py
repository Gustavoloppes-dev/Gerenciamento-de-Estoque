from cadastro import cadastrar_produto, cadastrar_categoria, consultar_produto
from movimentacoes import registrar_entrada, registrar_saida
from relatorios import gerar_relatorio_movimentacoes, consultar_historico_movimentacoes, gerar_relatorio_estoque_limite

cadastrar_categoria(1, "Eletrônicos")
cadastrar_categoria(2, "Livros")


cadastrar_produto(1, "Smartphone", "Eletrônicos", 50, 1200.00, "Fornecedor X", "Deposito A")
cadastrar_produto(2, "Câmera", "Eletrônicos", 20, 800.00, "Fornecedor Y", "Deposito B")


registrar_entrada(1, 10)  
registrar_saida(2, 5)     

produto = consultar_produto(1)
if produto:
    print(f"Produto consultado: {produto.nome}, Estoque: {produto.quantidade}")


gerar_relatorio_movimentacoes(1)


consultar_historico_movimentacoes()

gerar_relatorio_estoque_limite()