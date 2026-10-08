"""
Entregável de Desenvolvimento em Python - Semana 04 (Sprint 4)
Sistema de Gestão de Produtos, Estatísticas e Filtragem.
"""


def sistema_produtos():
    # -------------------------------------------------------------------------
    # 1. CADASTRO DE PRODUTOS
    # Python: Estruturas dinâmicas (listas e dicionários/listas compostas)
    # -------------------------------------------------------------------------
    # EQUIVALÊNCIA EM PORTUGOL:
    # algoritmo "CadastroDeProdutos"
    # var
    #    nomes: vetor[1..50] de caractere
    #    precos: vetor[1..50] de real
    #    categorias: vetor[1..50] de caractere
    #    qtd_produtos, i: inteiro
    # inicio
    #    escreva("Quantos produtos deseja cadastrar? ")
    #    leia(qtd_produtos)
    #    para i de 1 ate qtd_produtos faca
    #       escreva("Nome do produto: ")
    #       leia(nomes[i])
    #       escreva("Preço: ")
    #       leia(precos[i])
    #       escreva("Categoria: ")
    #       leia(categorias[i])
    #    fimpara
    # fimalgoritmo
    # -------------------------------------------------------------------------

    produtos = []

    print("=== CADASTRO DE PRODUTOS ===")
    qtd_produtos = int(input("Quantos produtos deseja cadastrar? "))

    for i in range(qtd_produtos):
        print(f"\n--- Produto {i + 1} ---")
        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço (R$): "))
        categoria = input("Categoria: ").strip().title()

        # Armazenando produto como dicionário dentro da lista
        produtos.append(
            {"nome": nome, "preco": preco, "categoria": categoria}
        )

    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    # -------------------------------------------------------------------------
    # 2. FILTRAGEM POR PREÇO
    # Python: List comprehension / Filtro simples percorrendo a lista
    # -------------------------------------------------------------------------
    # EQUIVALÊNCIA EM PORTUGOL:
    # limite_preco: real
    # escreva("Exibir produtos com preço acima de: R$ ")
    # leia(limite_preco)
    # para i de 1 ate qtd_produtos faca
    #    se precos[i] > limite_preco entao
    #       escreval("Produto: ", nomes[i], " | Preço: R$ ", precos[i])
    #    fimse
    # fimpara
    # -------------------------------------------------------------------------

    print("\n" + "=" * 40)
    print("=== FILTRAGEM POR PREÇO ===")
    limite_preco = float(
        input("Listar produtos com preço acima de (R$): ")
    )

    produtos_filtrados = [p for p in produtos if p["preco"] > limite_preco]

    # -------------------------------------------------------------------------
    # 3. ORDENAÇÃO (Bubble Sort em Portugol vs sort/sorted em Python)
    # -------------------------------------------------------------------------
    # EQUIVALÊNCIA EM PORTUGOL (Método da Bolha / Bubble Sort):
    # var
    #    j: inteiro
    #    aux_nome, aux_cat: caractere
    #    aux_preco: real
    # inicio
    #    // Ordenação Crescente por Preço
    #    para i de 1 ate qtd_produtos - 1 faca
    #       para j de 1 ate qtd_produtos - i faca
    #          se precos[j] > precos[j + 1] entao
    #             // Troca os preços
    #             aux_preco <- precos[j]
    #             precos[j] <- precos[j + 1]
    #             precos[j + 1] <- aux_preco
    #             // Troca os nomes (para manter sincronizado)
    #             aux_nome <- nomes[j]
    #             nomes[j] <- nomes[j + 1]
    #             nomes[j + 1] <- aux_nome
    #             // Troca as categorias
    #             aux_cat <- categorias[j]
    #             categorias[j] <- categorias[j + 1]
    #             categorias[j + 1] <- aux_cat
    #          fimse
    #       fimpara
    #    fimpara
    # -------------------------------------------------------------------------

    # Criando nova lista ordenada (Decrescente) sem alterar a original
    produtos_ord_decrescente = sorted(
        produtos, key=lambda x: x["preco"], reverse=True
    )

    # Ordenando a lista original in-place (Crescente)
    produtos.sort(key=lambda x: x["preco"])

    # -------------------------------------------------------------------------
    # 4. CONJUNTO DE CATEGORIAS ÚNICAS (Set)
    # -------------------------------------------------------------------------
    # EQUIVALÊNCIA EM PORTUGOL (Simulação manual sem duplicações):
    # var
    #    categorias_unicas: vetor[1..50] de caractere
    #    qtd_unicas, k: inteiro
    #    ja_existe: logico
    # inicio
    #    qtd_unicas <- 0
    #    para i de 1 ate qtd_produtos faca
    #       ja_existe <- falso
    #       para k de 1 ate qtd_unicas faca
    #          se categorias[i] = categorias_unicas[k] entao
    #             ja_existe <- verdadeiro
    #          fimse
    #       fimpara
    #       se nao ja_existe entao
    #          qtd_unicas <- qtd_unicas + 1
    #          categorias_unicas[qtd_unicas] <- categorias[i]
    #       fimse
    #    fimpara
    # -------------------------------------------------------------------------

    categorias_unicas = set(p["categoria"] for p in produtos)

    # -------------------------------------------------------------------------
    # 5. TUPLA DE ESTATÍSTICAS (Imutável)
    # -------------------------------------------------------------------------
    # EQUIVALÊNCIA EM PORTUGOL:
    # var
    #    menor_p, maior_p, soma_p, media_p: real
    # inicio
    #    menor_p <- precos[1]
    #    maior_p <- precos[1]
    #    soma_p <- 0
    #    para i de 1 ate qtd_produtos faca
    #       se precos[i] < menor_p entao
    #          menor_p <- precos[i]
    #       fimse
    #       se precos[i] > maior_p entao
    #          maior_p <- precos[i]
    #       fimse
    #       soma_p <- soma_p + precos[i]
    #    fimpara
    #    media_p <- soma_p / qtd_produtos
    # -------------------------------------------------------------------------

    precos = [p["preco"] for p in produtos]
    menor_preco = min(precos)
    maior_preco = max(precos)
    media_preco = sum(precos) / len(precos)

    # Tupla contendo estatísticas imutáveis
    estatisticas = (menor_preco, maior_preco, media_preco)

    # -------------------------------------------------------------------------
    # 6. RELATÓRIO FINAL FORMATADO (Uso obrigatório de f-strings)
    # -------------------------------------------------------------------------
    print("\n" + "=" * 50)
    print(f"{'RELATÓRIO FINAL DE PRODUTOS':^50}")
    print("=" * 50)

    print("\n1. Produtos Acima de R$", f"{limite_preco:.2f}:")
    if produtos_filtrados:
        for p in produtos_filtrados:
            print(
                f"   - {p['nome']:<20} | Cat: {p['categoria']:<15} | R$ {p['preco']:.2f}"
            )
    else:
        print("   Nenhum produto atende ao critério de preço.")

    print("\n2. Produtos em Ordem Crescente de Preço (sort):")
    for p in produtos:
        print(
            f"   - {p['nome']:<20} | Cat: {p['categoria']:<15} | R$ {p['preco']:.2f}"
        )

    print("\n3. Produtos em Ordem Decrescente de Preço (sorted):")
    for p in produtos_ord_decrescente:
        print(
            f"   - {p['nome']:<20} | Cat: {p['categoria']:<15} | R$ {p['preco']:.2f}"
        )

    print("\n4. Categorias Únicas (Set):")
    for cat in categorias_unicas:
        print(f"   • {cat}")

    print("\n5. Estatísticas Gerais (Tupla imutável):")
    print(f"   • Menor Preço : R$ {estatisticas[0]:.2f}")
    print(f"   • Maior Preço : R$ {estatisticas[1]:.2f}")
    print(f"   • Preço Médio : R$ {estatisticas[2]:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    sistema_produtos()