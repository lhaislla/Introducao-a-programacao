n = input('\033[5;36;41mDigite algo: ')
print(type(n))

print(n.isnumeric())
#se o que foi digitado é alfanumerico

print(n.isalpha())
#se o que foi digitado é alfabetico

print(n.isdecimal())
#se o que foi digitado é um decimal

print(n.isspace())
#se o que foi digitado tem espaço

print(n.islower())
#se o que foi digitado é minusculo

print(n.isupper())
#se o que foi digitado é maiuscula

print(n.istitle())
#se o que foi digitado tem a primeira letra maiuscula e as outras minusculas

print(n.isidentifier())
#se o que foi digitado é um identificador valido
