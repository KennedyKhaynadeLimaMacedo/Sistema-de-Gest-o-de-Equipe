def gerar_relatorio(produtos):
    print("\n--- RELATÓRIO DO ESTOQUE ---")

    if not produtos:
        print("Nenhum produto cadastrado!")
        print("Valor total: R$ 0.00")
        print("Total de unidades: 0")
        return

    total = sum(p[2] * p[3] for p in produtos.values())
    unidades = sum(p[3] for p in produtos.values())

    print(f"Produtos cadastrados: {len(produtos)}")
    print(f"Total de unidades: {unidades}")
    print(f"Valor total: R$ {total:.2f}")

    print("\n--- ESTOQUE BAIXO (5 OU MENOS) ---")
    encontrou = False

    for p in produtos.values():
        if 0 < p[3] <= 5:
            print(f"{p[0]} - {p[3]} unidades")
            encontrou = True

    if not encontrou:
        print("Nenhum produto com estoque baixo.")

    print("\n--- SEM ESTOQUE ---")
    encontrou = False

    for p in produtos.values():
        if p[3] == 0:
            print(p[0])
            encontrou = True

    if not encontrou:
        print("Nenhum produto sem estoque.")