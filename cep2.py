import tkinter as tk
from tkinter import messagebox
import requests

def buscar_endereco():
    endereco = entry_endereco.get().strip()
    estado = entry_estado.get().strip()
    cidade = entry_cidade.get().strip()
    
    if endereco.isdigit():
        messagebox.showerror("Erro", "Digite um Endereço válido.")
        return

    url = f"https://viacep.com.br/ws/{estado}/{cidade}/{endereco}/json/"
    response = requests.get(url)
    
    if response.status_code == 200: 
        dados = response.json()
        dados = dados[0]
        
        if "erro" in dados:
            messagebox.showerror("Erro", "Endereço não encontrado.")
        else:
            cep = (
                f"CEP: {dados['cep']}"
            )
            label_resultado.config(text=cep)
    else:
        messagebox.showerror("Erro", "Erro na consulta ao ViaCEP.")

# Configurando a janela principal
root = tk.Tk()
root.title("Busca de CEP pelo Endereço")
root.geometry("300x400")

# Campo de entrada para o Endereço
label_endereco = tk.Label(root, text="Digite o Endereço:")
label_endereco.pack(pady=5)
entry_endereco = tk.Entry(root)
entry_endereco.pack(pady=5)

# Campo de entrada para a Cidade
label_cidade = tk.Label(root, text="Digite a Cidade:")
label_cidade.pack(pady=5)
entry_cidade = tk.Entry(root)
entry_cidade.pack(pady=5)

# Campo de entrada para o Estado
label_estado = tk.Label(root, text="Digite o Estado:")
label_estado.pack(pady=5)
entry_estado = tk.Entry(root)
entry_estado.pack(pady=5)

# Botão para buscar o endereço
botao_buscar = tk.Button(root, text="Buscar CEP", command=buscar_endereco)
botao_buscar.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Executando o loop da interface gráfica
root.mainloop()