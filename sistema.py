import PySimpleGUI as sg
from arquivo import *

sg.theme('LightGreen')

layout = [
    [sg.Text('MENU PRINCIPAL', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Button('CADASTRAR NOVO PRODUTO', size=(30, 1))],
    [sg.Button('ALTERAR PRODUTO', size=(30, 1))],
    [sg.Button('EXCLUIR PRODUTO', size=(30, 1))],
    [sg.Button('REGISTRAR COMPRA', size=(30, 1))],
    [sg.Button('REGISTRAR VENDA', size=(30, 1))],
    [sg.Button('CONSULTAR ESTOQUE', size=(30, 1))],
    [sg.Button('CONSULTAR VALOR ESTOQUE', size=(30, 1))],
    [sg.Text()],
    [sg.Exit('SAIR', size=(30, 1))]
    ]

# Janela
janela = sg.Window('Controle de Estoque').layout(layout).Finalize()


def pesquisa():
    consultar = [
        [sg.Text('Código: ', size=(15, 1)), sg.Input(key='-cod-')],
        [sg.Text()],
        [sg.OK('OK'), sg.Cancel('Cancelar')]
    ]
    window_consultar = sg.Window('PESQUISAR PRODUTO', consultar)
    evento, valor = window_consultar.read()
    window_consultar.close()
    busca = valor['-cod-']
    try:
        for p, e in enumerate(estoque):
            if e[0] == busca:
                return p
    except:
        return None


def cadastro_p():
    cadastro = [
        [sg.Text('Código: ', size=(15, 1)), sg.Input(key='-cod-')],
        [sg.Text('Nome: ', size=(15, 1)), sg.Input(key='-nome-')],
        [sg.Text('Quantidade: ', size=(15, 1)), sg.Input(key='-qtd-')],
        [sg.Text('Preço de Compra: ', size=(15, 1)), sg.Input(key='-prc-')],
        [sg.Text('Preço de Venda: ', size=(15, 1)), sg.Input(key='-prv-')],
        [sg.Text()],
        [sg.OK('Salvar'), sg.Cancel('Cancelar')]
    ]
    window_cadastro = sg.Window('CADASTRAR NOVO PRODUTO', cadastro)
    evento, valor = window_cadastro.read()
    window_cadastro.close()
    if evento == 'Salvar':
        estoque.append([valor['-cod-'], valor['-nome-'], valor['-qtd-'], valor['-prc-'], valor['-prv-']])
        grava()


def excluir_produto():
    if verifica_estoque():
        p = pesquisa()
        if p is not None:
            confirmar = [
                [sg.Text('DESEJA MESMO EXCLUIR?', size=(30, 1))],
                [sg.Text()],
                [sg.OK('Sim'), sg.Cancel('Não')]
            ]
            windows_confirmar = sg.Window('EXCLUIR PRODUTO', confirmar)
            evento, valor = windows_confirmar.read()
            windows_confirmar.close()
            if evento == 'Sim':
                estoque.pop(p)  # remove o item da lista
                grava()
                sg.Print('Produto excluido com sucesso!!')
        else:
            sg.Print('PRODUTO NÃO ENCONTRADO!!')


def alterar_cadastro():
    if verifica_estoque():
        p = pesquisa()
        if p is not None:
            alterar = [
                [sg.Text('Nome: ', size=(15, 1)), sg.Input(key='-nome-')],
                [sg.Text('Preço de Compra: ', size=(15, 1)), sg.Input(key='-prc-')],
                [sg.Text('Preço de Venda: ', size=(15, 1)), sg.Input(key='-prv-')],
                [sg.Text()],
                [sg.OK('Salvar'), sg.Cancel('Cancelar')]
            ]
            windows_alterar = sg.Window('ALTERAR CADASTRO', alterar)
            evento, valor = windows_alterar.read()
            windows_alterar.close()
            if evento == 'Salvar':
                estoque[p] = [estoque[p][0], valor['-nome-'], estoque[p][2], valor['-prc-'], valor['-prv-']]
                grava()
                sg.Print('Alteração gravada com sucesso!')
        else:
            sg.Print('PRODUTO NÃO ENCONTRADO!!')


def registrar_compra_venda(cv):
    if verifica_estoque():
        p = pesquisa()
        if p is not None:
            if cv == 1:
                compra = [
                    [sg.Text('Quantidade: ', size=(15, 1)), sg.Input(key='-qtd-')],
                    [sg.Text()],
                    [sg.OK('Salvar'), sg.Cancel('Cancelar')]
                ]
                windows_compra = sg.Window('COMPRA DE PRODUTO', compra)
                evento, valor = windows_compra.read()
                windows_compra.close()
                if evento == 'Salvar':
                    quantidade = int(estoque[p][2])
                    quantidade = quantidade + int(valor['-qtd-'])
                    estoque[p][2] = quantidade
                    grava()
                    sg.Print('Compra gravada com sucesso!')
            elif cv == 2:
                compra = [
                    [sg.Text('Quantidade: ', size=(15, 1)), sg.Input(key='-qtd-')],
                    [sg.Text()],
                    [sg.OK('Salvar'), sg.Cancel('Cancelar')]
                ]
                windows_compra = sg.Window('VENDA DE PRODUTO', compra)
                evento, valor = windows_compra.read()
                windows_compra.close()
                if evento == 'Salvar':
                    if int(estoque[p][2]) >= int(valor['-qtd-']):
                        quantidade = int(estoque[p][2])
                        quantidade = quantidade - int(valor['-qtd-'])
                        estoque[p][2] = quantidade
                        grava()
                        sg.Print('Venda gravada com sucesso!')
                    else:
                        sg.Print(f'Quantidade em estoque é inferior a quantidade que deseja vender!\n\n'
                                 f'Existem {estoque[p][2]} em estoque do produto: {estoque[p][1].upper()}')


def valor_estoque():
    if verifica_estoque():
        somac = 0.0
        somav = 0.0
        for i in estoque:
            qtd = int(i[2])
            valorc = float(i[3])
            valorv = float(i[4])
            somac = somac + (valorc * qtd)
            somav = somav + (valorv * qtd)
        valor_tot_estoque = [
            [sg.Text(f'Total no estoque preço de CUSTO: R$ {somac:.2f}')],
            [sg.Text(f'Total no estoque preço de VENDA: R$ {somav:.2f}')],
            [sg.Text(f'\nTotal de LUCRO: R$ {somav - somac:.2f}')],
            [sg.OK()]
        ]
        window_valor_estoque = sg.Window('VALOR TOTAL EM ESTOQUE', valor_tot_estoque)
        window_valor_estoque()
        window_valor_estoque.close()


def consultar_estoque():
    if verifica_estoque():
        for e in estoque:
            sg.Print(f'Código: {e[0]} \nNome: {e[1]} \nQuantidade: {e[2]} \nPreço de Compra: R$ {float(e[3]):.2f} \n'
                     f'Preço de Venda: R$ {float(e[4]):.2f}')
            sg.Print('-' * 70)


def verifica_estoque():
    if len(estoque) > 0:
        return True
    else:
        sg.Print('Não existe produtos em estoque!')
        return False


def main():
    while True:
        event, values = janela.read()
        if event == sg.WIN_CLOSED or event == 'SAIR':
            break
        elif event == 'CADASTRAR NOVO PRODUTO':
            cadastro_p()
        elif event == 'ALTERAR PRODUTO':
            alterar_cadastro()

        elif event == 'EXCLUIR PRODUTO':
            excluir_produto()

        elif event == 'REGISTRAR COMPRA':
            registrar_compra_venda(1)

        elif event == 'REGISTRAR VENDA':
            registrar_compra_venda(2)

        elif event == 'CONSULTAR ESTOQUE':
            consultar_estoque()

        elif event == 'CONSULTAR VALOR ESTOQUE':
            valor_estoque()


arq = 'estoque.txt'  # nome do arquivo .txt do estoque

if not arquivo_existe(arq):  # verificar se o arquivo existe, caso não exista crie
    criar_arquivo(arq)

le_estoque()
main()
