import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime

# Função para salvar o pedido em um arquivo JSON
#def salvar_chamado():

def atualizar_data():
    hoje = datetime.now().strftime("%d/%m/%Y")
    label_data.config(text=f"{hoje}")






# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Sistema de Registro de Chamados")

# Labels e Entries para os campos
label_nome = tk.Label(janela, text="Nome do Cliente:")
label_nome.grid(row=0, column=0)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

label_problema = tk.Label(janela, text="Problema:")
label_problema.grid(row=1, column=0)

lista = ["Problema de Rede", "Falha de Software", "Erro de Hardware", "Outro"]
tupla = ("Problema de Rede", "Falha de Software", "Erro de Hardware", "Outro")
comboboxEspecie = ttk.Combobox(janela, values=lista)
comboboxEspecie.grid(row=1, column=1)

label_descricao = tk.Label(janela, text="Descrição do problema:")
label_descricao.grid(row=2, column=0)

self_descricao = tk.Text(janela, height=5)
self_descricao.grid(row=2, column=1)

label_prioridade = tk.Label(janela, text="Prioridade:")
label_prioridade.grid(row=3, column=0)

lista1 = ["Alta", "Média", "Baixa"]
tupla1 = ("Alta", "Média", "Baixa")
comboboxEspecie = ttk.Combobox(janela, values=lista1)
comboboxEspecie.grid(row=3, column=1)

label_data1 = tk.Label(janela, text="Data de abertura:")
label_data1.grid(row=4, column=0)
label_data = tk.Label(janela)
label_data.grid(row=4, column=1)

label_numeroChamado = tk.Label(janela, text="Número do chamado:")
label_numeroChamado.grid(row=5, column=0)

# Botões organizados em duas linhas
#botao_salvar = tk.Button(janela, text="Salvar Pedido", width=20, command=salvar_chamado)
#botao_salvar.grid(row=5, column=0)

#botao_recuperar = tk.Button(janela, text="Recuperar Chamado", width=20, command=recuperar_chamado)
#botao_recuperar.grid(row=5, column=1)

#botao_novo_pedido = tk.Button(janela, text="Novo Chamado", width=20, command=limpar_campos)
#botao_novo_pedido.grid(row=6, column=0)

atualizar_data()
janela.mainloop()