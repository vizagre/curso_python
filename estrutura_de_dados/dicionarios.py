frutas = {
    'maçã': 2.5,
    'banana': 1.8,
    'laranja': 3.0,
    'uva': 4.2  
}

print (frutas)  # Imprimindo o dicionário completo
print(frutas['maçã'])  # Acessando o preço da maçã
print(frutas.keys())  # Imprimindo as chaves do dicionário
print(frutas.values())  # Imprimindo os valores do dicionário

frutas['pera'] = 2.0  # Adicionando um novo item ao dicionário
print(frutas)  # Imprimindo o dicionário atualizado

del frutas['banana']  # Removendo o item 'banana' do dicionário
print(frutas)  # Imprimindo o dicionário após a remoção 

print(frutas.items())  # Imprimindo os itens do dicionário (chave-valor)

print(frutas.get('uva'))  # Acessando o preço da uva usando get()
print(frutas.get('abacaxi', 'Fruta não encontrada'))  # Tentando acessar uma fruta que não existe, com valor padrão