estoque = []


def arquivo_existe(nome):
    """ verificação se arquivo existe """
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """ criar novo arquivo """
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo!\033[0;0m')


def le_estoque():
    """ carregar o 'estoque.txt' no sistema e copia para a lista estoque """
    with open('estoque.txt', 'rt', encoding='utf-8') as arquivo:
        estoque.clear()  # limpando a lista antes de carregar o estoque.txt
        for i in arquivo.readlines():
            cod, nome, qtd, pc, pv = i.strip().split("#")
            estoque.append([cod, nome, qtd, pc, pv])
    arquivo.close()  # fechando o arquivo após o uso
    return 0


def grava():
    """ função para gravar o 'estoque.txt' (nome 'estoque.txt' predefinido) """
    with open('estoque.txt', 'wt+', encoding='utf-8') as arquivo:
        for e in estoque:
            arquivo.write(f'{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n')
    arquivo.close()  # fechando o arquivo após o uso
    return 0
