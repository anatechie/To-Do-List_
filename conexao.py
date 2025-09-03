import sqlite3
from datetime import datetime

con = sqlite3.connect('todolist.db')
cursor = con.cursor() #cursor executa comandos SQL dentro da conxao

#cria tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    Titulo TEXT NOT NULL,
    Descricao TEXT,
    Status INTEGER DEFAULT 0,
    Prioridade INTEGER DEFAULT 2, 
    Categoria TEXT,
    Data_Criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    Data_Limite DATETIME, 
    Data_Conclusao DATETIME
)
""");

con.commit()

cursor.execute("""
INSERT INTO tarefas(titulo, descricao,prioridade, categoria, data_limite,
                    data_conclusao)
                    VALUES(?,?,?,?,?,?)
""", (titulo, descricao, prioridade, categoria, data_limite, data_conclusao));

con.commit()

cursor.execute("""
SELECT * FROM tarefas
""");
tarefas = cursor.fetchall()
    for t in tarefas:
        print(t)


con.commit()

cursor.execute("""
UPDATE tarefas SET Status = 1, Data_Conclusao = ? WHERE id= ?
""", (datetime.now(), tarefa_id));

print(f"Tarefa {id} marcada como concluída")
con.commit()

cursor.execute("""
UPDATE tarefas SET Status = 0, Data_Conclusao = NULL WHERE id =?
""")

