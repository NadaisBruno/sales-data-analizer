import streamlit as st
import re
import pandas as pd
from database import insert_clients_db
from database import list_clients_db
from database import remove_clients_db
from database import update_clients_db
from database import filter_clients_db


# --------------------------- Clientes -------------------------------------------

# def adicionar clientes mais respetivas validacoes para os respetivos campos
def adicionar_clients(nome_client, empresa_client, email_client, telefone_client, faturacao_total_client):
    # validação para o nome
    if not nome_client.strip():
        st.error("O campo 'Nome' não pode ficar vazio")
        return

    # A-Z = Aceita intervalo de maiusculas
    # a-z = Aceita intervalo de minusculas
    # À-ÿ = Aceita intervalo de caracteres acentuados
    # ' = Aceita apóstrofo
    # + = Permite varios caracteres; sem este + validava nomes com um unico caractere
    if not re.fullmatch(r"[A-Za-zÀ-ÿ' ]+", nome_client):
        st.error("O campo 'nome' contém carateres inválidos e não pode conter elementos númericos")
        return

    # validação para a empresa
    if not empresa_client.strip():
        st.error("O campo 'empresa' não pode ficar vazio")
        return

    # validação para o email
    if not email_client.strip():
        st.error("O campo 'email' não pode ficar vazio")
        return

    if "@" not in email_client or "." not in email_client:
        st.error("O campo 'email' deve conter '@' e '.' ")
        return

    # validação para o telefone
    if not telefone_client.strip():
        st.error("O campo 'telefone' não pode ficar vazio")
        return

    # \+? = aceita '+' no início para números internacionais e pode aparecer até uma vez ou nenhuma
    if not re.fullmatch(r"\+?[0-9]+", telefone_client):
        st.error("O campo 'telefone' só deve conter digitos e, opcionalmente, '+' no ínicio")
        return

    # vamos buscar funcao da base de dados para inserir o novo cliente
    insert_clients_db(
        nome_client,
        empresa_client,
        email_client,
        telefone_client,
        faturacao_total_client
    )

    st.success("Cliente adicionado com sucesso!")


# def para remover clientes
def remover_clients(remove_client_id):
    remove_clients_db(remove_client_id)

    st.success("Cliente removido com sucesso!")


# def para actualizar/editar clientes
def editar_clientes(client_id, nome_client, empresa_client, email_client, telefone_client, faturacao_total_client):
    # validação para o nome
    if not nome_client.strip():
        st.error("O campo 'Nome' não pode ficar vazio")
        return

    # A-Z = Aceita intervalo de maiusculas
    # a-z = Aceita intervalo de minusculas
    # À-ÿ = Aceita intervalo de caracteres acentuados
    # ' = Aceita apóstrofo
    # + = Permite varios caracteres; sem este + validava nomes com um unico caractere
    if not re.fullmatch(r"[A-Za-zÀ-ÿ' ]+", nome_client):
        st.error("O campo 'nome' contém carateres inválidos e não pode conter elementos númericos")
        return

    # validação para a empresa
    if not empresa_client.strip():
        st.error("O campo 'empresa' não pode ficar vazio")
        return

    # validação para o email
    if not email_client.strip():
        st.error("O campo 'email' não pode ficar vazio")
        return

    if "@" not in email_client or "." not in email_client:
        st.error("O campo 'email' deve conter '@' e '.' ")
        return

    # validação para o telefone
    if not telefone_client.strip():
        st.error("O campo 'telefone' não pode ficar vazio")
        return

    # \+? = aceita '+' no início para números internacionais e pode aparecer até uma vez ou nenhuma
    if not re.fullmatch(r"\+?[0-9]+", telefone_client):
        st.error("O campo 'telefone' só deve conter digitos e, opcionalmente, '+' no ínicio")
        return

    update_clients_db(
        client_id,
        nome_client,
        empresa_client,
        email_client,
        telefone_client,
        faturacao_total_client
    )

    st.success("Cliente atualizado com successo!")


# def para a filtragem de clientes
def filtrar_clientes(filter_nome, filter_empresa, filter_email):
    resultados = filter_clients_db(filter_nome, filter_empresa, filter_email)
    return resultados


# ---- titulo ----
st.title("CRM TSS - Cibersegurança")

opcoes = st.selectbox(
    "Por favor escolha uma opçao",
    ("Clientes", "Leads/Oportunidades")
)

# ------------- criar clients -----------------------
form_clients = st.form("Clientes", clear_on_submit=True)

titulo_clientes = form_clients.title("Clientes")

nome = form_clients.text_input("Nome")
empresa = form_clients.text_input("Empresa")
email = form_clients.text_input("Email")
telefone = form_clients.text_input("Telefone")
faturacao_total = form_clients.number_input("Faturação total", min_value=0)

botao_clients = form_clients.form_submit_button("Criar cliente")
if botao_clients:
    #
    adicionar_clients(nome, empresa, email, telefone, faturacao_total)

# subtitulo para a tabela de clientes
st.subheader("Lista de Clientes")

# ---------------- remover clients -----------------------------


# vamos buscar todos os clientes a base de dados
listar_clientes = list_clients_db()

dataframe_clientes = pd.DataFrame(
    listar_clientes,
    columns=["ID", "Nome", "Empresa", "Email", "Telefone", "Faturação Total"]
)

# mostra todos os clientes numa tabela
# selection_mode permite selecionar uma linha na tabela
# faz o streamlit reagir à seleção
tabela_clientes = st.dataframe(dataframe_clientes, on_select="rerun", selection_mode="single-row")

# verifica se foi selecionada uma linha na tabela
if tabela_clientes.selection.rows:

    # guarda o indice da linha selecionada
    indice = tabela_clientes.selection.rows[0]

    # usa o indice da linha anterior para ir buscar o cliente correspondente a lista
    cliente_selecionado = listar_clientes[indice]

    # o primeiro elemento do tuplo do cliente é o seu id
    id_cliente = cliente_selecionado[0]

    # criar o botao para remover o cliente selecionado
    botao_remover_clients = st.button("Remover cliente")

    # se o botao for clicado...
    if botao_remover_clients:
        # ...chama a funcao de remocao de clientes
        remover_clients(id_cliente)

    # ------------------- atualizar clientes ------------------------

    atualizar_nome = cliente_selecionado[1]
    atualizar_empresa = cliente_selecionado[2]
    atualizar_email = cliente_selecionado[3]
    atualizar_telefone = cliente_selecionado[4]
    atualizar_faturacao_total = cliente_selecionado[5]

    # criamos um novo formulario, agora para atualizar/editar os clientes
    form_atualizar_clients = st.form("Atualizar Clientes")

    # titulo do formulario
    titulo_atualizar_clientes = form_atualizar_clients.title("Atualizar Clientes")

    # 'value' mostra os dados atuais do cliente
    nome = form_atualizar_clients.text_input("Nome", value=atualizar_nome)
    empresa = form_atualizar_clients.text_input("Empresa", value=atualizar_empresa)
    email = form_atualizar_clients.text_input("Email", value=atualizar_email)
    telefone = form_atualizar_clients.text_input("Telefone", value=atualizar_telefone)
    faturacao_total = form_atualizar_clients.number_input("Faturação total", value=float(atualizar_faturacao_total),
                                                          min_value=float(0))

    botao_atualizar_clients = form_atualizar_clients.form_submit_button("Atualizar Cliente")
    if botao_atualizar_clients:
        editar_clientes(id_cliente, nome, empresa, email, telefone, faturacao_total)

# ---------------- filtrar clientes -----------------------

# Criamos um novo formulario para o processo de filtragem
form_filtrar_clients = st.form("Filtrar Clientes")

# Titulo do formulario
titulo_filtrar_clientes = form_filtrar_clients.title("Filtrar Clientes")

filtro_nome = form_filtrar_clients.text_input("Nome")
filtro_empresa = form_filtrar_clients.text_input("Empresa")
filtro_email = form_filtrar_clients.text_input("Email")

# botao filtrar clientes
botao_filtrar_clients = form_filtrar_clients.form_submit_button("Filtrar Clientes")
if botao_filtrar_clients:
    filtro = filtrar_clientes(filtro_nome, filtro_empresa, filtro_email)

    # criamos um dataframe com pandas para poder mostrar nomes nas colunas… sem isto o Streamlit mostra cabecalhos numerados
    dataframe_filtro = pd.DataFrame(
        filtro,
        columns=["ID", "Nome", "Empresa", "Email"]
    )

    st.dataframe(dataframe_filtro)

