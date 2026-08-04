import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from read_validate_csv import validate_csv
from csv_metrics import metrics
from html_report import relatorio_html
from graficos import graphics


def open_file():

    # askopenfilename devolve o caminho do ficheiro
    file = askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file:
        df = validate_csv(file)
        if df is None:
            return

        # calculo de todas as metricas do csv
        dict_metrics = metrics(df)

        # gera relatorio de HTML
        relatorio_html(dict_metrics)

        # gera o grafico utilizando os totais por produto
        graphics(dict_metrics["totais_produto"])

        print(dict_metrics)


root = tk.Tk()
root.title("Analisador de dados de vendas")  # titulo da janela
root.resizable(True, True)  # Ativa o redimensionamento da janela
root.geometry("800x600")

label = tk.Label(root, text="", font=("Arial", 15, "bold"), foreground="blue")
label.grid(row=0, column=0, columnspan=3, padx=50, pady=50)

# botao
button = tk.Button(root, text="Escolher ficheiro", command=open_file, background="white", foreground="blue")
button.grid(row=1, column=0, columnspan=3, padx=50, pady=50)

root.mainloop()


