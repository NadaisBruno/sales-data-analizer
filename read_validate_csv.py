from tkinter import messagebox
import pandas as pd


def validate_csv(file):
    df = pd.read_csv(file, encoding="utf-8", sep=";")
    print(df)

    # se o df estiver vazio mostra erro
    if df.empty:
        messagebox.showerror("Erro", "O ficheiro esta vazio")
        return None

    # verificamos se o CSV contem as colunas obrigatorias
    colunas_obrigatorias = ["Cliente", "Produto", "Quantidade", "Preço", "Data"]
    for coluna in colunas_obrigatorias:
        if coluna not in df.columns:
            messagebox.showerror("Erro", "O ficheiro deve conter as colunas: Cliente, Produto, Quantidade, Preço e Data")
            return None

    # converter a coluna data para o tipo datetime
    # qualquer valor que nao seja uma data valida é tranformado em NAT(not a time)
    # com coerce o program apresenta erro imediato e transforma esse valor numa data invalida(NaT)
    df["Data"] = pd.to_datetime(df["Data"], dayfirst=True, errors="coerce")
    if df["Data"].isna().any():
        messagebox.showerror("Erro", "Certifique-se que as datas estão no formato válido(DD-MM-AAAA ou AAAA-MM-DD)")
        return None

    # preço -----
    df["Preço"] = pd.to_numeric(df["Preço"], errors="coerce")
    if df["Preço"].isna().any():
        messagebox.showerror("Erro", "Certifique-se que todos os valores desta coluna são numeros válidos,"
                                     "usando ponto como separador")
        return None

    if (df["Preço"] <= 0).any():
        messagebox.showerror("Erro", "Existem valores negativos na coluna Preço")
        return None

    # quantidade ----
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce")
    if df["Quantidade"].isna().any():
        messagebox.showerror("Erro", "Certifique-se que os valores desta coluna são numeros inteiros")
        return None


    if (df["Quantidade"] <= 0).any():
        messagebox.showerror("Erro", "Existem valores negativos ou nulos na coluna 'Quantidade'")
        return None

    if (df["Quantidade"] % 1 != 0).any():
        messagebox.showerror("Erro", "A coluna 'Quantidade' não pode conter valores decimais")
        return None

    # produto -----
    if (df["Produto"].str.strip() == "").any():
        messagebox.showerror("Erro", "A coluna 'Produto' contem valores vazios ou apenas espaços em branco")
        return None

    if df["Produto"].isna().any():
        messagebox.showerror("Erro", "A coluna 'Produto' contem valores em falta.Preencha todas as celulas antes de continuar")
        return None

    # cliente -----
    if df["Cliente"].isna().any():
        messagebox.showerror("Erro", "A coluna 'Cliente' contem valores em falta.Preencha todas as celulas antes de continuar")
        return None

    if (df["Cliente"].str.strip() == "").any():
        messagebox.showerror("Erro", "A coluna 'Cliente' contem valores vazios ou apenas espaços em branco")
        return None

    print(df.shape)

    # se o df nao estiver vazio devolve-o com os dados
    return df


