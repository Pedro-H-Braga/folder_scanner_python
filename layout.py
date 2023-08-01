import PySimpleGUI as sg

def frontend():
    sg.theme('DarkBrown') 

    layout = [     
                [sg.Text('INFORME A PASTA *COMPARTILHADA* COM O CLIENTE:')], 
                [sg.FolderBrowse('PASTA COMPARTILHADA',key='-compartilhada-')],

                [sg.Text('INFORME A PASTA *INTERNA* DA EMPRESA:')], 
                [sg.FolderBrowse('-------PASTA INTERNA-------',key='-interna-')],

                [sg.Text('INFORME A DATA NA SEGUINTE FORMATAÇÃO: 202X/MES(NUMERICO)*/*')],
                [sg.InputText(key='-data_ver-')],
                
                [sg.Button('Verificar'), sg.Button('Sair')] ]
    
    window = sg.Window('MOVIMENTACAO DE ARQUIVOS DOS CLIENTES', layout)

    return window

def fecha_janela(event):
    if event == sg.WIN_CLOSED or event == 'Sair': 
        exit()