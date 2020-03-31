''' Manipulação d e arquivos em python:
    - Modos:
        * r = somente leitura
        * r+ = leitura e escrita . O texto é inserido no inicio do arquivo.
        * w = Escrita apagando(truncando) o conteúdo existente no arquivo
        * w+ =Leitura e escrita. O arquivo é criado, se não existir; se existir é truncado. O texto é inserido no inicio do arquivo.
        * a = Escrita,preservando o conteúdo existente(append). O arquivo é criado, se não existir. O texto é inserido no final do arquivo
        * b = Modo binário
        * + Atualização - leitura e escrita
        * x = Abre o arquivo para criação, falhando s eo arquivo já existir
        Podemos combinar: r+,w+,w+b
        A função open retorna um objeto de um arquivo usada com dois argumentos : o nome do arquivo e o modo

para ler o conteúdo de um arquivo :
    - arq.read(size)= O tamanho de linhas do arquivo
    - arq.readlines() = Lê um única linha do arquivo
    - arq.write = escreve o conteúdo de uma string para o arquivo
    -arq.seek(posição)= manipula o ponteiro que indica a posição em que a linha irá apontar
Para escrever em um arquivo:
    -
'''