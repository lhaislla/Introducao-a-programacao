# Função voto que recebe como parametro ano de nascimento de uma pessoa
# Retorna um valor literal indicando se apessoa tem voto:
# Negado
# Opcional
# Obrigatorio  nas eleições
from datetime import datetime
nasc = int(input('Em que nao você naceu? '))
ano = datetime.now().year
idade = ano - nasc

def voto(idade):
    if  16 <= idade <= 18 or idade >= 65:
        return  ('Voto Opcional')
    if idade >= 18:
        return  ('Voto Obrigatorio')
    else:
        return  ('Voto Negado')
print(f'Com {idade} o voto é {voto(idade)}')