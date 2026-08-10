

def relatorio_html(dict_metrics):

    with open("relatorio.html", "w", encoding="utf-8") as f:

        f.write(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            
            <style>
            img {{
                display: block;
                margin-left: auto;
                margin-right: auto;
            }}
            
            #id_formadores {{
                text-align: center;
                color: grey;
            }}
            
            #metricas_gerais {{
            border: 3px solid grey;
            margin-top: 40px;
            margin-bottom: 40px;
            padding-top: 25px;
            padding-right: 25px;
            padding-bottom: 25px;
            padding-left: 25px;
            background-color: lightgrey;
            }}
            
            #totais_por_produto {{
            border: 3px solid grey;
            margin-top: 40px;
            margin-bottom: 40px;
            padding-top: 25px;
            padding-right: 25px;
            padding-bottom: 25px;
            padding-left: 25px;
            background-color: lightgrey;
            }}
            
            #grafico_tabela {{ 
            display: flex;
            justify-content: flex-start;
            }}
            
            #top_3_produtos {{
            border: 3px solid grey;
            margin-top: 40px;
            margin-bottom: 40px;
            padding-top: 25px;
            padding-right: 25px;
            padding-bottom: 25px;
            padding-left: 25px;
            background-color: lightgrey;
            }}
            
            table, th, td {{
            border: 1px solid;
            padding: 10px;
            text-align: center;
            }}
            
            tr:hover {{background-color: grey;}}
            
            body {{
            font-family: Arial;
            }}    
            
            h1 {{
            margin-top: 50px;
            margin-bottom: 50px;
            text-shadow: 2px 2px 20px black;
            }}
            
            </style>
        </head>
        <body>
        <img src="Formadores_Day_Traders.png" width="500" height="333">
        <h1 id="id_formadores">Formadores Day Traders</h1>
        
        <h2>Relatório de Vendas</h2>
        
        <div id="metricas_gerais">
            <h2>Métricas Gerais</h2>
            <p>Total de vendas: {dict_metrics["total_vendas"]}</p>
            <p>Total quantidade: {dict_metrics["total_quantidade"]}</p>
            <p>Total faturado: {dict_metrics["total_faturado"]}</p>
            <p>Média de vendas: {dict_metrics["media_vendas"]}</p>
            <p>Média de quantidade: {dict_metrics["media_quantidade"]}</p>
        </div>
        """)

        # criação da tabela para totais por produto e o respetivo cabeçalho
        f.write("""
        
        <!-- div principal onde e criada a caixa cinzenta com a seccao toda(titulo, tabela e grafico) -->
        <div id="totais_por_produto">
            <h2>Totais por Produto</h2>
            <!-- div interno usado apenas para alinhar a tabela e o grafico(o titulo fica de fora deste div para nao interferir com o layout) -->
            <div id="grafico_tabela">    
                <table>
                    <tr>
                        <th>Produto</th>
                        <th>Total</th>
                    </tr>
                """)


        # calculo dos totais por produto
        # contem varios produtos, logo precisamos de os percorrer um a um
        for produto, total in dict_metrics["totais_produto"].items():
            f.write(f"""
            <tr>
                <td>{produto}</td>
                <td>{total} €</td>
            </tr>
            """)

        f.write("""

        </table>
        <img src="grafico_vendas.png" width="600" height="433">
        </div>
        </div>
        """)


        f.write("""
        
        <div id="top_3_produtos">
        <h2>Top 3 Produtos</h2>
        
        <table>
            <tr>
                <th>Produto</th>
                <th>Total</th>
            </tr>
            
        """)

        # calculo dos top 3 produtos
        for produto, total in dict_metrics["top_3_produtos"].items():
            f.write(f"""
            <tr>
                <td>{produto}</td>
                <td>{total} €</td>
            </tr>
            """)

        f.write("""
        </table>
        </div>
        """)

        f.write("""
        </body>
        </html>
        """)
