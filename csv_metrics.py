def metrics(df):
    linhas = df.shape[0]
    total_quantidade = df["Quantidade"].sum()

    # Criação de uma nova coluna Total Venda
    df["Total_Venda"] = df["Quantidade"] * df["Preço"]

    # total faturado arredondado a duas casas decimais
    total_faturado = round(df["Total_Venda"].sum(), 2)

    # calculo da media de vendas arredondado a duas casas decimais // mean() soma todos os valores e divide pelo número de linhas
    media_vendas = round(df["Total_Venda"].mean(), 2)

    # calculo da media da quantidade
    media_quantidade = df["Quantidade"].mean()

    # calculo dos totais por produto arredondado a duas casas decimais
    totais_produto = df.groupby("Produto")["Total_Venda"].sum()

    # top 3 dos produtos mais vendidos em faturacao
    top_3_produtos = df.groupby("Produto")["Total_Venda"].sum().sort_values(ascending=False).head(3)

    # dicionario das metricas para ser enviado para o HTML
    dict_metrics = {
        "total_vendas": linhas,
        "total_quantidade": total_quantidade,
        "total_faturado": total_faturado,
        "media_vendas": media_vendas,
        "media_quantidade": media_quantidade,
        "totais_produto": totais_produto,
        "top_3_produtos": top_3_produtos
    }
    return dict_metrics
