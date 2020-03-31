#Programa que lê o ano de nascimento de  um jovem
#Calcula a idade
#-se ele ainda vai se alistar ao serviço militar.
#-Se é hora de alistar
#-Se já passou do tempo de alistamento
#-Mostra o tempo que falta  ou que  se passsou do prazo

from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('\033[3;36;mDigite o ano de seu nascimento: '))
idade = ano_atual - ano_nascimento
tempo = 18 - idade
if idade < 18:
    print('\033[5;36;mVocê precisrá se alista daqui a: {} anos'.title().format(tempo))
elif idade == 18:
    print('\033[5;36;mÉ hora de se alistar no serviço militar obrigatório!'.title())
else:
    tempo = idade -18
    print('\033[3;36;mQuem nasceu no ano de {} tem {}anos em {}'.title().format(ano_nascimento,idade,ano_atual))
    print('Você já deveria ter se alistado há {} anos'.format(tempo))
    print('Seu alistamento foi a:{} ano(s) atrás'.format(tempo))
