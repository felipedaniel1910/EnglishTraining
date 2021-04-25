import time
import os
import playsound
import speech_recognition as sr
from gtts import gTTS

step_list = ['1.mp3','2.mp3','3.mp3','4.mp3','5.mp3','6.mp3','7.mp3','8.mp3','9.mp3','10.mp3']
i = 0

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
    print(dir_path)
    dir = os.listdir(dir_path)
    for file in dir:
        file = file.strip()
        if file == text.strip():
            os.remove(file)
          
x = 0
while(x<5):
    text = input("Texto: ")
    speak(text)

