#importando bibliotecas
import Database                             #faz referencia ao novo script ->Database<-
from tkinter import messagebox
#permite utilizar caixa de aviso (texto)
#from tkinter import *                      #Biblioteca para desenvolvimento de interface (não utilizada até o momento)

engl = []                                   #Lista onde as palavras em Inglês serão armazenadas quando carregadas do BD
port = []                                   #Lista onde as palavras em português serão armazenadas quando carregadas do BD

def RegisterToDataBase():                   #Função Responsável por cadastrar novas palavras no BD
    Engl = str(input("Write the word in English: "))        #Variavel local 
    Port = str(input("Digite a palavra em Português: "))    #Variavel local
    
    if (Port == "" or Engl == ""):          #Reporta uma mensagem de erro caso algum campo seja deixado vazio
            messagebox.showerror(title="Register Error", message="Não Deixe Nenhum Campo Vazio. Preenche Todos os Campos")
    
    else:
        Database.cursor.execute(""" 
        INSERT INTO Words(Engb,Portb) VALUES(?,?)
        """ ,(Engl,Port))                   #Abre o BD para inserção e posiciona o cursor na primeira linha vazia
        Database.conn.commit()              #Salvar as alterações- Commit salva
        messagebox.showinfo(title="Save Info", message="Palavra Cadastrada Com Sucesso")


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
        print("{} , {}".format(row[1],row[2]))
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
    
#RegisterToDataBase()
GetWord()
