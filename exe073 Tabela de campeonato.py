# 20 primeiros colocados na tabela do campeonato brasileiro de fotebol
# Pela ordem de colocação
# Moostre apenas os 5 primeiros colocados
# Mostre os últimos 4 colocados da tabela
# Mostre uma lista com os times em ordem alfabetica
# Mostre em que posição na tabela esta o time da chapecoense

times = ('', 'Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'São Paulo', 'Atlético-MG', 'Athletico-Pr','Cruzeiro', 'Botafogo', 'Santos', 'Bahia','Fluminense','Corinthians','Chapecoense', 'Ceará', 'Vasco','Sport', 'América-MG', 'Vitória', 'Paraná')
cinco = times[1:6]
ordem =sorted(times)
ultimos4 = times [16:21]
chap= times.index('Chapecoense')
print('\033[;32;m='*50)
print('\033[;31;m Informações do Brasileirão:')
print('\033[;32;m='*50)
print(f'\033[;31;m Lista de Times do Brasileirão: {times}')
print('\033[;32;m='*50)
print('\033[;31;m Os cinco primeiro colocados:')
print(cinco)
print('\033[;32;m='*50)
print('\033[;31;m Os quatro últimos colocados na tabela:')
print(ultimos4)
print('\033[;32;m='*50)
print(f'\033[;31;m Times em ordem alfabetica: {ordem}')
print('\033[;32;m='*50)
print(f'\033[;31;mA Chapecoense está na {chap}° posição')
print('\033[;32;m='*50)


