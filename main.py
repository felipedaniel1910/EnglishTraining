#Bibliotecas para que o programa pronucie as palavras
import Database                             #faz referencia ao novo script ->Database<-
from tkinter import messagebox              #permite utilizar caixa de aviso (texto)
import time
import os
import playsound                            #utilizado para reproduzir pronuncia
import speech_recognition as sr
from gtts import gTTS                       #utilizado para reproduzir pronuncia

#Biblioteca para geração de valores aleatórios
from random import randint 

engl = []                                   #Lista onde as palavras em Inglês serão armazenadas quando carregadas do BD
port = []                                   #Lista onde as palavras em português serão armazenadas quando carregadas do BD


step_list = ['1.mp3','2.mp3','3.mp3','4.mp3','5.mp3',
             '6.mp3','7.mp3','8.mp3','9.mp3','10.mp3']
i = 0

hits = 0
misses = 0

def RegisterToDataBase():                   #Função Responsável por cadastrar novas palavras no BD
    Engl = str(input("\n Write the word in English: ")).lower()        #Variavel local 
    Port = str(input(" Digite a palavra em Português: ")).lower()    #Variavel local
    
    if (Port == "" or Engl == ""):          #Reporta uma mensagem de erro caso algum campo seja deixado vazio
            messagebox.showerror(title="Register Error", message="Não Deixe Nenhum Campo Vazio. Preenche Todos os Campos")
    
    else:
        Database.cursor.execute(""" 
        INSERT INTO Words(Engb,Portb) VALUES(?,?)
        """ ,(Engl,Port))                   #Abre o BD para inserção e posiciona o cursor na primeira linha vazia
        Database.conn.commit()              #Salvar as alterações- Commit salva
        #messagebox.showinfo(title="Save Info", message="Palavra Cadastrada Com Sucesso")


def GetWord():                              #Função responsável por puxar os dados salvos no BD para o programa

    Database.cursor.execute("""
        SELECT * FROM Words
        """)                                #Abre o BD para leitura e posiciona o cursor na primeira linha
    
    #global engl                             #Avisa a função que se trata de uma variável global
    #global port                             #Avisa a função que se trata de uma variável global

    while(1):                               #Repete até que seja quebrado (break)
        
        row = Database.cursor.fetchone()    #row recebe a linha onde o cursor esta posicionado
        if row == None:                     #Se a linha for vazia
            break                           #Interrompe o while
        engl.append(row[1])                 #Adiciona o item 1 da lista row na lista engl
        port.append(row[2])                 #Adiciona o item 2 da lista row na lista port
    
    #Usado se quisermos restringir os itens selecionados (usando WHERE) 
    '''Database.cursor.execute("""
    SELECT * FROM Words
    WHERE (Engb = ? AND Portb = ?)
    """,(word1,word2))
    VerifyWord = Database.cursor.fetchone()
    print("Selecionou")
    print(VerifyWord)'''

def speak(text):
    tts = gTTS(text=text, lang="en")
    text = text+".mp3"
    global i
    
    #Encontra o diretório
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = os.listdir(dir_path)
    #print(dir_path) #imprime o diretório se necessário
    for file in dir: #Verifica se o nome do arquivo ja existe
        file = file.strip()
        if file == text.strip():
            text = step_list[i]
            i+=1
    
    filename = text
    tts.save(filename)
    playsound.playsound(filename)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir = os.listdir(dir_path)
    for file in dir:
        file = file.strip()
        if file == text.strip():
            os.remove(file)

while(1):

    os.system('cls') # Limpa a tela

    print("\n")
    print("-=-"*20)
    print("         Welcome to Felipe's English Training...")
    print("-=-"*20)
    
    print("\n Escolha uma das opções abaixo: ")

    
    menu = 0 #inicia a variavel com valor 0
    try:
        while (menu!=1 and menu!=2 and menu!=3 and menu!=4):
            menu = int(input("\n 1- Cadastrar palavras.\n 2- Jogar\n 3- Consultar BD.\n 4- Sair "))
    except: None

    if menu == 1:

        RegisterToDataBase()

    if menu == 2:

        if len(engl) != 0: #verifica se os dados já foram extraídos do BD
            None
        else: 
            GetWord()
        
        while(1):

            os.system('cls') # Limpa a tela

            print("\n")
            print("-=-"*20)
            print("         Welcome to Felipe's English Training...")
            print("-=-"*20)

            if len(engl) == 0:
                print(" Não existem palavras cadastradas, por favor realize o cadastro!")
                input("\n Press enter to continue...")
                break
            
            loop = int(input("\n Número de rodadas: ")) # Número de vezes que repetirá até que pergunte-se se o usuário deseja sair

            for i in range (loop):

                    
                word = randint(0,len(engl)-1) # Sorteia qual palavra será visualizada
                indice = randint(0,1)

                if indice == 0: # Mostra a palavra em Ingles
                    answer = str(input("\n Translate the word *{}* to portuguese: ".format(engl[word]))).lower()
                    
                    speech=0 #inicia a variavel com valor 0
                    try: 
                        while (speech!=1 and speech!=2):
                            speech = int(input(" Hear pronunciation: 1-YES 2-NOT: "))
                    except: None

                    if speech == 1:
                        speak(engl[word])
                        
                    if answer == port[word]: # Se a resposta estiver correta
                        print(" Sounds Good!")
                        hits+=1
                    else:
                        print(" Ops... You made a mistake!")
                        print(" The correct word is {}.".format(port[word]))
                        misses+=1

                else: # Mostra a palavra em Portugues
                    answer = str(input("\n Traduza a palavra *{}* para inglês: ".format(port[word]))).lower()

                    if answer == engl[word]:
                        print(" Beleza!")
                        hits+=1
                    else:
                        print(" Opa... Você cometeu um erro!")
                        print(" A palavra correta é {}.".format(engl[word]))
                        misses+=1

            again = 0 #inicia a variavel com valor 0
            try: 
                while (again!=1 and again!=2):
                    again = int(input("\n Voce gostaria de continuar? 1-SIM  2-NÃO: "))
            except: 
                again = 2

            if again == 2:
                print("\n Você ACERTOU {} palavras e ERROU {} palavras...".format(hits,misses))
                print(" Volte sempreee :) ")

                input("\n Press enter to finish...")
                break

    if menu == 3:

        os.system('cls') # Limpa a tela

        print("\n")
        print("-=-"*20)
        print("         Welcome to Felipe's English Training...")
        print("-=-"*20)
        
        if len(engl) != 0: #verifica se os dados já foram extraídos do BD
            None
        else: GetWord()

        print('\nO BD contém {} dados!'.format(len(engl)))

        consulta = 0
        try:
            while(consulta!=1 and consulta!= 2):
                consulta = int(input('\nQue tipo de consulta deseja fazer?\n\n 1- Visualizar dados.\n 2- Sair. '))
        except: 
            None

        if consulta == 1:
            for i in range (0,len(engl)):
                print('\n{} - En word: {}\n{} - Pt word: {}'.format(i,engl[i],i, port[i]))
            input('\nPressione ENTER para continuar...')

        else: 
            None
  
    if menu == 4:
        print("\n Saindo em 5 segundos...")
        time.sleep(5)
        break
    

                

        
            
        
        
