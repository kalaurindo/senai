import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime

# Função para salvar o pedido em um arquivo JSON
def salvar_chamado():
    nome_cliente = entry_nome.get()
    problema = comboboxProblema.get()
    descricao = self_descricao.get(1.0, tk.END)
    prioridade = comboboxPrioridade.get()
    data = datetime.now().strftime("%d/%m/%Y")
    numero_chamado = int(label_numeroChamado1.cget("text"))

    if not nome_cliente or not problema or not self_descricao or not descricao or not prioridade or not data:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return
    # Verifica se o arquivo JSON já existe
    if os.path.exists("chamado.json"):
        with open("chamado.json", "r") as arquivo:
            chamados = json.load(arquivo) 
    else:
        chamados = []

    # Adiciona o novo pedido
    chamados.append(chamado)

      # Estrutura do chamado
    chamado = {
        "nome_cliente": nome_cliente,
        "problema": problema,
        "descricao": descricao,
        "prioridade": prioridade,
        "data": data,
        "numero_chamado": numero_chamado,
    }

    # Salva no arquivo JSON
    with open("chamado.json", "w") as arquivo:
        json.dump(chamados, arquivo, indent=4)

    messagebox.showinfo("Sucesso", "Chamado salvo com sucesso!")

#função para gerar proximo numero de chamado
def gerar_numero():
    if os.path.exists("chamado.json"):
        with open("chamado.json", "r") as arquivo:
            chamados = json.load(arquivo) 

        # Procura o pedido pelo numero do chamado
        for chamado in chamados:
            numero = chamado ["numero_chamado"]
        numero = numero + 1
        return numero


    # Limpa os campos após salvar
    limpar_campos()

# Função para exibir um pedido específico
def recuperar_chamado():
    if os.path.exists("chamado.json"):
        numero_chamado = simpledialog.askstring("Recuperar Chamado", "Digite o número do chamado:")
        if not numero_chamado:
            return

        with open("chamado.json", "r") as arquivo:
            chamados = json.load(arquivo) 

        # Procura o pedido pelo numero do chamado
        for chamado in chamados:
            if chamado["numero_chamado"] == int(numero_chamado):
                entry_nome.delete(0, tk.END)
                entry_nome.insert(0, chamado["nome_cliente"])
                comboboxProblema.delete(0, tk.END)
                comboboxProblema.insert(0, chamado["problema"])
                self_descricao.delete("1.0", tk.END)
                self_descricao.insert("1.0", chamado["descricao"])
                comboboxPrioridade.delete(0, tk.END)
                comboboxPrioridade.insert(0, chamado["prioridade"])
                label_data.config(text= chamado["data"])
                label_numeroChamado1.config(text= chamado["numero_chamado"])
                return

        messagebox.showinfo("Chamado não encontrado", f"Pedido com número '{numero_chamado}' não encontrado.")
    else:
        messagebox.showinfo("Sem Chamados", "Nenhum chamado cadastrado até o momento.")


def limpar_campos():
    entry_nome.delete(0, tk.END)
    comboboxProblema.delete(0, tk.END)
    self_descricao.delete("1.0", tk.END)
    comboboxPrioridade.delete(0, tk.END)
    label_data.config(text= datetime.now().strftime("%d/%m/%Y"))
    label_numeroChamado1.config(text= gerar_numero())
    entry_nome.focus()

def atualizar_data():
    hoje = datetime.now().strftime("%d/%m/%Y")
    label_data.config(text=f"{hoje}")

largura = 60
largura1 = 30

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Sistema de Registro de Chamados")

# Labels e Entries para os campos
label_nome = tk.Label(janela, text="Nome do Cliente:", width=largura1)
label_nome.grid(row=0, column=0, sticky='ew')

entry_nome = tk.Entry(janela, width=largura)
entry_nome.grid(row=0, column=1, sticky='ew')

label_problema = tk.Label(janela, text="Problema:", width=largura1)
label_problema.grid(row=1, column=0, sticky='ew')

lista = ["Problema de Rede", "Falha de Software", "Erro de Hardware", "Outro"]
tupla = ("Problema de Rede", "Falha de Software", "Erro de Hardware", "Outro")
comboboxProblema = ttk.Combobox(janela, values=lista, width=largura)
comboboxProblema.grid(row=1, column=1, sticky='ew')

label_descricao = tk.Label(janela, text="Descrição do problema:", width=largura1)
label_descricao.grid(row=2, column=0, sticky='ew')

self_descricao = tk.Text(janela, height=3, width=largura)
self_descricao.grid(row=2, column=1, sticky='ew')

label_prioridade = tk.Label(janela, text="Prioridade:", width=largura1)
label_prioridade.grid(row=3, column=0, sticky='ew')

lista1 = ["Alta", "Média", "Baixa"]
tupla1 = ("Alta", "Média", "Baixa")
comboboxPrioridade = ttk.Combobox(janela, values=lista1, width=largura)
comboboxPrioridade.grid(row=3, column=1, sticky='ew')

label_data1 = tk.Label(janela, text="Data de abertura:", width=largura1)
label_data1.grid(row=4, column=0, sticky='ew')
label_data = tk.Label(janela, width=largura)
label_data.grid(row=4, column=1, sticky='ew')

label_numeroChamado = tk.Label(janela, text="Número do chamado:", width=largura1)
label_numeroChamado.grid(row=5, column=0, sticky='ew')
label_numeroChamado1 = tk.Label(janela, text= "0", width=largura)
label_numeroChamado1.grid(row=5, column=1, sticky='ew')

# Botões organizados em duas linhas
botao_salvar = tk.Button(janela, text="Salvar Chamado", width=20, command=salvar_chamado)
botao_salvar.grid(row=6, column=0, sticky='ew')

botao_recuperar = tk.Button(janela, text="Recuperar Chamado", width=20, command=recuperar_chamado)
botao_recuperar.grid(row=6, column=1, sticky='ew')

botao_novo_pedido = tk.Button(janela, text="Novo Chamado", width=20, command=limpar_campos)
botao_novo_pedido.grid(row=7, column=0, sticky='ew')

atualizar_data()
janela.mainloop()