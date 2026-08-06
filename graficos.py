import matplotlib.pyplot as plt


def graphics(totais_produto):
    x = []
    y = []
    for produto, total in totais_produto.items():
        x.append(produto)
        y.append(total)

    for i in range(len(x)):
        # labels(valores dos artigos) centradas dentro das barras
        plt.text(i, y[i], y[i], ha='center', bbox=dict(facecolor='green', alpha=0.5))

    font1 = {'family': 'arial', 'color': 'grey', 'size': 22}
    font2 = {'family': 'arial', 'color': 'blue', 'size': 15}

    plt.title("Totais de Vendas por Produto", fontdict=font1)
    plt.xlabel("Produtos", fontdict=font2)
    plt.ylabel("Total", fontdict=font2)

    # grafico de barras
    plt.bar(x, y)

    # roda ligeiramente as labels do eixo dos x
    plt.xticks(rotation=10)

    # permite o ajuste automatico das margens do grafico para que nada fique cortado
    plt.tight_layout()

    # guardar o grafico
    plt.savefig("grafico_vendas.png")

    # mostrar grafico
    plt.show()
