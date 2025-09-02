import sqlite3

con = sqlite3.connect('todolist.db')
cursor = con.cursor() #cursor executa comandos SQL dentro da conxao

#cria tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS 
""")
