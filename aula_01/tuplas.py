tupla = ("Python", "Java", "C++", "JavaScript")
print(tupla)
print(tupla[0])  # Acessando o primeiro elemento
print(tupla[1:3])  # Acessando um intervalo de elementos
print(len(tupla))  # Obtendo o tamanho da tupla
print("Java" in tupla)  # Verificando se um elemento está na tupla  

# Tuplas são imutáveis, então não podemos modificar seus elementos
# tupla[0] = "Ruby"  # Isso causará um erro     

# No entanto, podemos criar uma nova tupla concatenando outras tuplas
nova_tupla = tupla + ("Ruby", "Go")
print(nova_tupla)   

# Podemos também usar tuplas para desempacotar valores
linguagem1, linguagem2, linguagem3, linguagem4 = tupla
print(linguagem1)  # Python
print(linguagem2)  # Java
print(linguagem3)  # C++
print(linguagem4)  # JavaScript 

