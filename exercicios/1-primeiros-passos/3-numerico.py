data_nascimento = '05-10-1976'
idade = 36
altura = 1.84
peso = 82.50


# Descubra o tipo de dado de cada variável acima
print(type(data_nascimento)) #<class 'str'>
print(type(idade)) #<class 'int'>
print(type(altura)) #<class 'float'>

# Realize uma operação entre dados do tipo string e inteiro
print('Lucas'*3) #LucasLucasLucas

# Realize uma operação entre dados do tipo inteiro e float
idade_float = idade * altura
print(idade_float) #88.32

#Realize uma operação entre dados do tipo inteiro, float e string
taxa_metabolica_basal = 66 + (13.7 * peso) + (5 * altura * 100) - (6.8 * idade)
mensagem = f'Com {idade} anos, {altura}m de altura e {peso}kg, sua TMB é {taxa_metabolica_basal:.2f} kcal/dia.'
print(taxa_metabolica_basal) # 1871.45
print(mensagem) # Com 36 anos, 1.84m de altura e 82.5kg, sua TMB é 1871.45 kcal/dia.