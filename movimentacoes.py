from datetime import datetime


def movimentar(produtos, historico, tipo):
    cod = input("Código do produto: ").strip()

    if cod not in produtos:
        print("Produto não encontrado!")
        return

    try:
        qtd = int(input("Quantidade: "))
    except ValueError:
        print("Digite uma quantidade inteira!")
        return

    p = produtos[cod]

    if qtd <= 0:
        print("Quantidade inválida!")
        return

    if tipo == "Saída" and qtd > p[3]:
        print("Estoque insuficiente!")
        return

    if tipo == "Entrada":
        p[3] += qtd
    else:
        p[3] -= qtd

    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    historico.append({
        "data": data,
        "tipo": tipo,
        "nome": p[0],
        "quantidade": qtd
    })

    print(f"{tipo} registrada com sucesso!")


def mostrar_historico(historico):
    if not historico:
        print("Nenhuma movimentação registrada!")
        return

    print("\n--- HISTÓRICO ---")

    for item in historico:
        print(f"\nData: {item['data']}")
        print(f"Tipo: {item['tipo']}")
        print(f"Produto: {item['nome']}")
        print(f"Quantidade: {item['quantidade']}")