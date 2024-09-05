import tkinter as tk
from tkinter import messagebox

def calcular():
    num1 = float(entryQuantidade.get())
    num2 = float(entryPreco.get())
    resultado = num1 * num2
    #messagebox.showinfo("Total do pedido", f"O valor total do pedido é: {resultado}")
    labelTotalPedido.config(text = f"R$ {resultado:.2f}")

janela = tk.Tk()
janela.title("Sistema IRango 1.0")

labelNome = tk.Label(janela, text ="Faça seu pedido:",) 
labelNome.pack(padx=50, pady=30)

# ***** Cadastro do tipo de lanche ********
labelLanche = tk.Label(janela, text ="Lanche",) 
labelLanche.pack(padx=50, pady=5)

entryLanche = tk.Entry(janela, width=100) 
entryLanche.pack(padx=50, pady=5)

# ***** Cadastro de quantidade ********
labelQuantidade = tk.Label(janela, text ="Quantidade",) 
labelQuantidade.pack(padx=50, pady=5)

entryQuantidade = tk.Entry(janela, width=50) 
entryQuantidade.pack(padx=50, pady=5)

# ***** Cadastro de Preço ********
labelPreco = tk.Label(janela, text ="Preço",) 
labelPreco.pack(padx=50, pady=5)

entryPreco = tk.Entry(janela, width=50) 
entryPreco.pack(padx=50, pady=5)

# ***** Cadastro de total do pedido ********
labelTotal = tk.Label(janela, text ="Total do pedido") 
labelTotal.pack(padx=50, pady=20)

labelTotalPedido = tk.Label(janela, width=50) 
labelTotalPedido.pack(padx=50, pady=20)

buttonCalcular = tk.Button(janela, text = "Calcular total", command=calcular)
buttonCalcular.pack(padx=50, pady=10)

janela.geometry("500x500")
janela.mainloop()