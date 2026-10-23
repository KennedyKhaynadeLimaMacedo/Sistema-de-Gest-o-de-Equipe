from produtos import (
    cadastrar, listar, buscar, atualizar,
    remover, ordenar, categorias
)
from movimentacoes import movimentar, mostrar_historico
from relatorios import gerar_relatorio

produtos = {}
historico = []

while True:
    print("\n--- SISTEMA DE ESTOQUE ---")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar produto")
    print("5 - Remover produto")
    print("6 - Entrada de estoque")
    print("7 - Saída de estoque")
    print("8 - Relatórios")
    print("9 - Histórico")
    print("10 - Ordenar produtos")
    print("11 - Listar categorias")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        cadastrar(produtos)
    elif op == "2":
        listar(produtos)
    elif op == "3":
        buscar(produtos)
    elif op == "4":
        atualizar(produtos)
    elif op == "5":
        remover(produtos)
    elif op == "6":
        movimentar(produtos, historico, "Entrada")
    elif op == "7":
        movimentar(produtos, historico, "Saída")
    elif op == "8":
        gerar_relatorio(produtos)
    elif op == "9":
        mostrar_historico(historico)
    elif op == "10":
        ordenar(produtos)
    elif op == "11":
        categorias(produtos)
    elif op == "0":
        print("Sistema encerrado. Até mais!")
        break
    else:
        print("Opção inválida!")