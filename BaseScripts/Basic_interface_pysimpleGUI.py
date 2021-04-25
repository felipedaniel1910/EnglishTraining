import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('GreenMono') #muda o stilo da janela
        # Layout
        layout = [
        [sg.Text('Nome',size=(5,0)),sg.Input(size=(30,0), key='nome')],    #linha 1
        [sg.Text('Idade',size=(5,0)), sg.Input(size=(30,0),key='idade')],  #linha 2
        [sg.Text('Em quais cursos deseja se inscrever?')],
        [sg.Checkbox('Inglês',key='ing'),sg.Checkbox('Espanhol',key='esp')],
        [sg.Text('Qual o tipo de ensino?')],
        [sg.Radio('EAD','ensino',key='ead'),sg.Radio('Presencial','ensino',key='presencial')],
        [sg.Text('Qual seu nível atual de inglês?')],
        [sg.Slider(range=(0,100),default_value=0,orientation='h',size=(15,20),key='nivelIngles')],
        [sg.Text('Qual seu nível atual de espanhol?')],
        [sg.Slider(range=(0,100),default_value=0,orientation='h',size=(15,20),key='nivelEspanhol')],
        [sg.Button("Enviar Dados")],     
        #logs - mostram as informações que estão sendo extraídas
        [sg.Output(size=(40,10))] 
        ]
        # Janela
        self.janela = sg.Window("Dados do Aluno").layout(layout)
        # Extrair os dados da tela
        #self.button, self.values = self.janela.Read() coloca aqui se for rodar 1 vez apenas

    def Iniciar(self):
        #print(self.values) mostra todos os dados em um dicionário
        while True: #mantem a janela aberta
            #Extrair informações da tela
            self.button, self.values = self.janela.Read() #faz rodar apenas 1 vez no loop e aguardar novos dados
            nome = self.values['nome']
            idade = self.values['idade']
            estudar_ingles = self.values['ing']
            estudar_espanhol = self.values['esp']
            ensino_ead = self.values['ead']
            ensino_presencial = self.values['presencial']
            nivel_ingles = self.values['nivelIngles']
            nivel_espanhol = self.values['nivelEspanhol']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Estudar Inglês: {estudar_ingles}')
            print(f'Estudar Espanhol: {estudar_espanhol}')
            print(f'Ensino EAD: {ensino_ead}')
            print(f'Ensino Presencial: {ensino_presencial}')
            print(f'Nível Inglês: {nivel_ingles}')
            print(f'Nível Espanhol: {nivel_espanhol}')

tela = TelaPython()
tela.Iniciar()