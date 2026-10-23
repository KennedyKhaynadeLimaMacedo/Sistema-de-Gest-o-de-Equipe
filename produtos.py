
def cadastrar(produtos):
    cod = input("Código: ").strip()

    if not cod or cod in produtos:
        print("Código vazio ou já cadastrado!")
        return

    nome = input("Nome: ").strip()
    cat = input("Categoria: ").strip()

    try:
        preco = float(input("Preço: R$ ").replace(",", "."))
        qtd = int(input("Quantidade: "))

        if not nome or not cat or preco <= 0 or qtd < 0:
            print("Dados inválidos!")
            return

        produtos[cod] = [nome, cat, preco, qtd]
        print("Produto cadastrado!")

    except ValueError:
        print("Digite valores válidos!")


def listar(produtos):
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    for cod, p in produtos.items():
        print(f"\nCódigo: {cod}")
        print(f"Nome: {p[0]}")
        print(f"Categoria: {p[1]}")
        print(f"Preço: R$ {p[2]:.2f}")
        print(f"Quantidade: {p[3]}")

        if p[3] == 0:
            print("Produto sem estoque!")


def buscar(produtos):
    busca = input("Código, nome ou categoria: ").lower().strip()
    encontrou = False

    for cod, p in produtos.items():
        if (busca == cod.lower()
                or busca in p[0].lower()
                or busca in p[1].lower()):
            print(f"\n{cod} - {p[0]} | {p[1]}")
            print(f"Preço: R$ {p[2]:.2f} | Estoque: {p[3]}")
            encontrou = True

    if not encontrou:
        print("Produto não encontrado!")


def atualizar(produtos):
    cod = input("Código: ").strip()

    if cod not in produtos:
        print("Produto não encontrado!")
        return

    nome = input("Novo nome (Enter mantém): ").strip()
    cat = input("Nova categoria (Enter mantém): ").strip()
    preco = input("Novo preço (Enter mantém): ").strip()

    if nome:
        produtos[cod][0] = nome

    if cat:
        produtos[cod][1] = cat

    if preco:
        try:
            valor = float(preco.replace(",", "."))
            if valor <= 0:
                print("Preço inválido!")
                return
            produtos[cod][2] = valor
        except ValueError:
            print("Preço inválido!")
            return

    print("Produto atualizado!")


def remover(produtos):
    cod = input("Código para remover: ").strip()

    if cod in produtos:
        del produtos[cod]
        print("Produto removido!")
    else:
        print("Produto não encontrado!")


def ordenar(produtos):
    if not produtos:
        print("Nenhum produto cadastrado!")
        return

    print("1 - Nome")
    print("2 - Preço")
    print("3 - Quantidade")
    op = input("Ordenar por: ")

    indice = {"1": 0, "2": 2, "3": 3}.get(op)

    if indice is None:
        print("Opção inválida!")
        return

    for p in sorted(produtos.values(), key=lambda x: x[indice]):
        print(f"{p[0]} - R$ {p[2]:.2f} - Estoque: {p[3]}")


def categorias(produtos):
    if not produtos:
        print("Nenhum produto cadastrado!")
        return

    lista = sorted(set(p[1] for p in produtos.values()))

    for cat in lista:
        print(f"\nCategoria: {cat}")

        for p in produtos.values():
            if p[1] == cat:
                print(f" - {p[0]}")