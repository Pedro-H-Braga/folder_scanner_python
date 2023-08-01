
# --------------------------------------------------------
# REQUERIMENTOS DE BIBLIOTECAS NO ARQUIVO requirements.txt
# pip install os, PySimpleGUI, glob
# --------------------------------------------------------


import os, sys, subprocess, glob, PySimpleGUI as sg
from layout import frontend, fecha_janela

# Janela de exibição para os inputs
window = frontend()

while True:
    event, values = window.read() 
    fecha_janela(event)

    evento_compartilhada = values['-compartilhada-']
    evento_interna = values['-interna-']        
    pt_comp = evento_compartilhada
    pt_int = evento_interna

    data_verif = values['-data_ver-'] 

    path_remoto = str(f'{pt_comp}')
    path_local  = str(f'{pt_int}')

    arq_remoto = sorted(list(glob.iglob(path_remoto + f'**/**/{data_verif}*/*', recursive=True)))

    pos = 0 
    for nome in arq_remoto: 
       arq_remoto[pos] = nome[len(path_remoto):]
       pos += 1
    
    
    arq_local  = sorted(list(glob.iglob(path_local + f'**/**/{data_verif}*/*', recursive=True)))
    
    pos = 0
    for nome in arq_local: 
       arq_local[pos] = nome[len(path_local):]
       pos += 1
    
    arq_dif   = sorted(list(set(arq_remoto).difference(set(arq_local))))
    
    arq_lista = [] 
    temp_clientes_duplicados = []
    clientes_lista = []
    extensoes = '.ini'    

    for posicao_dif in arq_dif:
      arq_lista.append(posicao_dif)  

    ''' MÉTODO UTILIZADO PARA CONSEGUIR PEGAR STRING '\' SEM BUG DE PALAVRA RESERVADA DO PYTHON'''
    barra = '\\'
    barra = barra[-1:]
    try:
      txt_final = open('movimentacoes_clientes.txt', 'w', encoding='utf-8') 
    except Exception as e:
       sg.popup(f'ERROR ao abrir o arquivo de movimentacoes dos clientes: \n{e}')
       txt_final.close()
       fecha_janela(event)
       sys.exit()
    # Pegando os nomes dos clientes 
    for posicao_lista in arq_lista:
          if extensoes not in posicao_lista:
            for indice,letra in enumerate(posicao_lista):
               if letra == barra and indice != 0:
                  posicao_lista = posicao_lista[:indice]
                  temp_clientes_duplicados.append(posicao_lista)

    clientes_lista = list(set(temp_clientes_duplicados))
    clientes_lista.sort()
    for clientes in clientes_lista:
       txt_final.write(f'{clientes}\n')

    txt_final.close()
    
    sg.popup('MOVIMENTACOES OCORRIDAS')

    cam = os.getcwd()
    fullPath = f'{cam}/movimentacoes_clientes.txt'
    
    try:
      subprocess.run(fullPath)        
    except Exception as e:
      sg.popup(f'Abra o arquivo localizado em: \n{fullPath}\n para acessar as movimentações')
      fecha_janela(event)
