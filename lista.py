estoque = ["caneta", "caderno", "borracha", "lápis"]
print(estoque)
#Adicionar novo item ao estoque
estoque.append("marcador")
print(estoque)

#Remover item do estoque
estoque.remove("lápis")
print(estoque)

#Verificar se um item está em estoque
print("marcador" in estoque) #Saída: True