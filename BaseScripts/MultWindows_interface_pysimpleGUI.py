import PySimpleGUI as sg

#criar layout
def janela_login():
    sg.theme('Reddit') #tema
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)

def janela_pedido():
    sg.theme('Reddit') #tema
    layout = [
        [sg.Text('Escolha o idioma')],
        [sg.Checkbox('Inglês',key='ing'), sg.Checkbox('Espanhol',key='esp')],
        [sg.Button('Voltar'), sg.Button('Escolher')]
    ]
    return sg.Window('Escolher idioma', layout=layout, finalize=True)

#criar janelas iniciais

janela1, janela2 = janela_login(), None

#criar loop

while True:
    window,event,values = sg.read_all_windows()
    #quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    #quando queremos ir para a próxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Escolher':
        if values['ing'] == True and values['esp']== True:
           sg.popup('Você escolheu estudar inglês e espanhol!')
        elif values['ing'] == True:
           sg.popup('Você escolheu estudar inglês!')
        elif values['esp'] == True:
           sg.popup('Você escolheu estudar espanhol!')
