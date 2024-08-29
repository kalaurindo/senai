import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def mensagem():
    messagebox.showinfo("Dados","Cadastro realizado com sucesso!")
    janela.destroy() #fecha a janela

janela = tk.Tk()
janela.title("Cadastro Pet")

#**********Cadastro Nome do tutor********************
labelNome = tk.Label(janela, text = "Nome do tutor do Pet")
labelNome.pack(padx=50, pady=10)

entryNome = tk.Entry(janela, width=100)
entryNome.pack(padx=50,pady=5)

#**********Cadastro Nome do pet********************
labelNomePet = tk.Label(janela, text = "Nome do Pet")
labelNomePet.pack(padx=50, pady=10)

entryNomePet = tk.Entry(janela, width=100)
entryNomePet.pack(padx=50,pady=5)

#**********Cadastro Nascimento do Pet********************
labelNascimentoPet = tk.Label(janela, text = "Data de Nascimento do Pet")
labelNascimentoPet.pack(padx=50, pady=10)

entryNascimentoPet = tk.Entry(janela, width=100)
entryNascimentoPet.pack(padx=50,pady=5)

#**********Cadastro Espécie do Pet********************
labelEspecie = tk.Label(janela, text = "Espécie do Pet")
labelEspecie.pack(padx=50, pady=10)

lista = ["", "Cachorro", "Gato", "Pássaro", "Outro"]
tupla = ("", "Cachorro", "Gato", "Pássaro", "Outro")
comboboxEspecie = ttk.Combobox(janela, values=lista)
comboboxEspecie.pack(padx=50,pady=0)

#**********Cadastro Raça********************
labelRaca = tk.Label(janela, text = "Raça do Pet")
labelRaca.pack(padx=50, pady=10)

entryRaca = tk.Entry(janela, width=100)
entryRaca.pack(padx=50,pady=5)

buttonSalvar = tk.Button(janela, text="Salvar",command=mensagem)
buttonSalvar.pack(padx=50, pady=30)

janela.geometry("600x500")

janela.mainloop()


