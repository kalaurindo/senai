import tkinter as tk
from tkinter import messagebox

def mensagem():
    messagebox.showinfo("Dados",f"{entryNome.get()};\ntel: {entryTelefone.get()}\n\nConfirme seus dados?")
    janela.destroy() #fecha a janela

janela = tk.Tk()
janela.title("Cadastro de Cliente")

# ***** Cadastro do nome do Cliente ********
labelNome = tk.Label(janela, text ="Nome") #font=("Arial",10), fg="white", bg="black") *** para mudar estilo da fonte
labelNome.pack(padx=50, pady=5)

entryNome = tk.Entry(janela, width=100) 
entryNome.pack(padx=50, pady=5)

# ***** Cadastro do telefone do Cliente ********
labelTelefone = tk.Label(janela, text ="Telefone")
labelTelefone.pack(padx=50, pady=5)

entryTelefone = tk.Entry(janela, width=100) 
entryTelefone.pack(padx=50, pady=5)

# ***** Cadastro do e-mail do Cliente ********
labelEmail = tk.Label(janela, text ="e-mail:")
labelEmail.pack(padx=50, pady=5)

entryEmail = tk.Entry(janela, width=100) 
entryEmail.pack(padx=50, pady=5)

buttonSalvar = tk.Button(janela, text="Salvar",command=mensagem)
buttonSalvar.pack(padx=50, pady=30)

janela.geometry("400x300")

janela.mainloop()
