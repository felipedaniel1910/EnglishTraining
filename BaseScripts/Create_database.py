import sqlite3                                      #Biblioteca utilizada para manipular o BD

conn = sqlite3.connect('UserData.db')               #Conecta o BD (ou cria caso isso não exista no diretório)

cursor = conn.cursor()                              #variavel cursor receber a posição do cursor no BD

cursor.execute("""
CREATE TABLE IF NOT EXISTS Words (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Engb TEXT NOT NULL,
    Portb TEXT NOT NULL
);
""")                                                #Criação da tabela no BD se não existir

#print("Conectado ao Banco de Dados")                #Aviso de conexão bem sucedida
