#Bibliotecas necessárias
import Database                             #faz referencia ao novo script ->Database<-
from tkinter import messagebox              #permite utilizar caixa de aviso (texto)
import time
import os
import playsound                            #utilizado para reproduzir pronuncia
import speech_recognition as sr
from gtts import gTTS                       #utilizado para reproduzir pronuncia
from tkinter import *                       #utilizado para front-end (interface) 
from tkinter import ttk                     #utilizado para front-end (interface)

#Biblioteca para geração de valores aleatórios
from random import randint

    
def GetWord():                              #Função responsável por puxar os dados salvos no BD para o programa

    Database.cursor.execute("""
        SELECT * FROM Words
        """)                                #Abre o BD para leitura e posiciona o cursor na primeira linha
    
    global engl                             #Avisa a função que se trata de uma variável global
    global port                             #Avisa a função que se trata de uma variável global

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

#=======criar nossa janela========
jan= Tk()                                   #cria a janela
jan.title("Felipe's English Training")      #define o nome do app (que aparece na parte superior)
jan.geometry("600x700")                     #dimensão da janela
jan.configure(background= "white")          #cor do fundo
jan.resizable(width=False, height=False)    #janela não ajustavel
jan.iconbitmap(default="Icons/Captain-America.ico")  #icone do app

#========Wifgets================
LeftFrame = Frame(jan, width=100, height=700, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=495, height=700, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

#=======Escrita para usuário-BEM VINDO========
Welcome = Label(RightFrame, text= "Welcome to Felipe's English", font=("Century Gothic",25), bg="MIDNIGHTBLUE",fg="White") #fg é a cor de fonte
Welcome.place(x=20, y=30)

#=======Escrita para usuário-MENU========
Menu = Label(RightFrame, text= "Escolha uma das opções abaixo:", font=("Century Gothic",20), bg="MIDNIGHTBLUE",fg="White") #fg é a cor de fonte
Menu.place(x=20, y=90)


def ScreenToRegister():                     #Muda para tela de registro de palavra


    #Removendo Widgets de Menu
    Welcome.place(x=1000)                   #Tira widget da tela
    Menu.place(x=1000)                      #Tira widget da tela
    Register.place(x=1000)                  #Tira widget da tela
    Play.place(x=1000)                      #Tira widget da tela
    Quit.place(x=1000)                      #Tira widget da tela
    

    #Criando Widgets desejados
    #=======Escrita para usuário-REGISTRANDO========
    Registering = Label(RightFrame, text= "Efetuando o Registro", font=("Century Gothic",25), bg="MIDNIGHTBLUE",fg="White") #fg é a cor de fonte
    Registering.place(x=20, y=30)
    #Inserindo Widget para coleta de palavra em ingles
    EnglLabel = Label(RightFrame, text="Palavra em Inglês:", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    EnglLabel.place(x=20, y=140)
    #Entrada de dados
    EnglEntry = ttk.Entry(RightFrame, width=20)
    EnglEntry.place(x=330, y=152)
    #Inserindo Widget para coleta de palavra em portugues
    PortLabel = Label(RightFrame, text="Palavra em Português:", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    PortLabel.place(x=20, y=175)
    #Entrada de dados
    PortEntry = ttk.Entry(RightFrame, width=20)
    PortEntry.place(x=330, y=187) 


    #print("scre {} , {}".format(Engl,Port))

   
    def RegisterToDataBase():                   #Função Responsável por cadastrar novas palavras no BD

        Engl = EnglEntry.get() 
        Port = PortEntry.get()
        
        print("reg {} , {}".format(Engl,Port))
        
        if (Port == "" or Engl == ""):          #Reporta uma mensagem de erro caso algum campo seja deixado vazio
                messagebox.showerror(title="Register Error", message="Não Deixe Nenhum Campo Vazio. Preenche Todos os Campos")
        
        else:
            Database.cursor.execute(""" 
            INSERT INTO Words(Engb,Portb) VALUES(?,?)
            """ ,(Engl,Port))                   #Abre o BD para inserção e posiciona o cursor na primeira linha vazia
            Database.conn.commit()              #Salvar as alterações- Commit salva
            #messagebox.showinfo(title="Save Info", message="Palavra Cadastrada Com Sucesso")


    #========Cria um botao-CONFIRMAR-=========
    Confirm = ttk.Button(RightFrame, text="Confirmar", width = 20, command=RegisterToDataBase)
    Confirm.place(x=170, y=235)
    
    def BackToMenu():
        #Removendo Widgets de Cadastro
        Registering.place(x=1000)
        EnglLabel.place(x=1000)
        PortLabel.place(x=1000)
        EnglEntry.place(x=1000)
        PortEntry.place(x=1000)
        Confirm.place(x=1000)
        Back.place(x=1000)
        
        #Mostrando Widgets desejados
        Welcome.place(x=20)
        Menu.place(x=20)
        Register.place(x=20)
        Play.place(x=20)
        Quit.place(x=20)
        
    Back = ttk.Button(RightFrame, text="Voltar", width = 20, command=BackToMenu)
    Back.place(x=170, y=275)
    

    jan.mainloop()                          #Atualiza a tela

#==============BOTÃO-OPÇÃO-1=================
Register = ttk.Button(RightFrame, text="Cadastrar Palavra", width = 30, command=ScreenToRegister) #command é uma funcao para atribuir funcao ao botao
Register.place(x=20, y=140)
    
def ScreenToNumber():
    #Removendo Widgets de Menu
    Welcome.place(x=1000)                   #Tira widget da tela
    Menu.place(x=1000)                      #Tira widget da tela
    Register.place(x=1000)                  #Tira widget da tela
    Play.place(x=1000)                      #Tira widget da tela
    Quit.place(x=1000)                      #Tira widget da tela

    #Criando Widgets desejados
    #=======Escrita para usuário-JOGANDO========
    Registering = Label(RightFrame, text= "Efetuando o Registro", font=("Century Gothic",25), bg="MIDNIGHTBLUE",fg="White") #fg é a cor de fonte
    Registering.place(x=20, y=30)
    #Inserindo Widget para coleta do numero de rodadas
    NumLabel = Label(RightFrame, text="Número de Rodadas:", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    NumLabel.place(x=20, y=140)
    #Entrada de dados
    NumEntry = ttk.Entry(RightFrame, width=20)
    NumEntry.place(x=330, y=152)

    def ScreenToPlay():
        #Removendo Widgets de Numero de jogadas
        Registering.place(x=1000)
        NumLabel.place(x=1000)
        NumEntry.place(x=1000)

        
        

 
#==============BOTÃO-OPÇÃO-2=================
Play = ttk.Button(RightFrame, text="Jogar", width = 30, command=ScreenToNumber) #command é uma funcao para atribuir funcao ao botao
Play.place(x=20, y=175)

#==============BOTÃO-OPÇÃO-3=================
Quit = ttk.Button(RightFrame, text="Sair", width = 30, command=ScreenToRegister) #command é uma funcao para atribuir funcao ao botao
Quit.place(x=20, y=210)

jan.mainloop()                          #Atualiza a tela


time.sleep(15)
engl = []                                   #Lista onde as palavras em Inglês serão armazenadas quando carregadas do BD
port = []                                   #Lista onde as palavras em português serão armazenadas quando carregadas do BD


step_list = ['1.mp3','2.mp3','3.mp3','4.mp3','5.mp3',
             '6.mp3','7.mp3','8.mp3','9.mp3','10.mp3']
i = 0

hits = 0
misses = 0


while(1):

    os.system('cls') # Limpa a tela

    print("\n")
    print("-=-"*20)
    print("         Welcome to Felipe's English Training...")
    print("-=-"*20)
    
    print("\n Escolha uma das opções abaixo: ")

    
    menu = 0
    while (menu!=1 and menu!=2 and menu!=3):
        menu = int(input("\n 1- Cadastrar palavras.\n 2- Jogar\n 3- Sair "))

    if menu == 1:

        RegisterToDataBase()

    if menu == 2:

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

                    speech = int(input(" Hear pronunciation: 1-YES 2-NOT: "))

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

            again = int(input("\n Voce gostaria de continuar? 1-SIM  2-NÃO: "))

            if again == 2:
                print("\n Você ACERTOU {} palavras e ERROU {} palavras...".format(hits,misses))
                print(" Volte sempreee :) ")

                input("\n Press enter to finish...")
                break

    if menu == 3:
        print("\n Saindo em 5 segundos...")
        time.sleep(5)
        break;
    

                

        
            
        
        
