frutas = ["uva", "banana", "laranja", "abacaxi"]    

tamanho = [len(fruta) for fruta in frutas]  
print(tamanho)

# Saída:
# [3, 6, 7, 8]  
# A expressão len(fruta) é avaliada para cada elemento da lista frutas, e o 
# resultado é armazenado na nova lista tamanho. 
# O resultado final é uma lista contendo os comprimentos de cada fruta.