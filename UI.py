import tkinter as tk
from tkinter import simpledialog, messagebox

# Configuração básica da interface gráfica
root = tk.Tk() #Cria janela
root.withdraw() #Esconde a janela principal

# Exemplo de uso
messagebox.showinfo("Entrada","Olá, mundo!") #showinfo mostra a janela
nomeDigitado = simpledialog.askstring("Identificação","Qual é o seu nome?") #askstring pergunta um texto
nomeSobrenome = simpledialog.askstring("Identificação","Qual é o seu sobrenome?")
idade = simpledialog.askstring("Idade","Qual é a sua idade?")
messagebox.showinfo("Saída",f"Seu nome é {nomeDigitado} {nomeSobrenome} e você tem {idade} anos") #mostra mensagem na janela