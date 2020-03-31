print('''\033[1;30;mEstruturas de controle:
    \033[1;36;m-Condições Aninhadas(Uma estrutura condicional dentro de outra)
            if: (Se)(1° parte)
            elif:(Se não se)(Usar quantas veze quiser)
            else: (Se não)(Usar apenas uma vez)
Exe:''')
nome = str(input('Digite seu nome: ')).title()
if nome== 'Lhaislla':
    print('\033[1;31;mQue nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('\033[1;31;mSeu nome é bem comum no Brasil')
else:
    print('\033[1;31;mSeu nome é bem normal. ')
print('\033[1;31;mTenha um bom dia, {}!'.format(nome))

            
        
 
 
 
 
 
 
 
 
 
 

