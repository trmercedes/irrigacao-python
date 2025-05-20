import sqlite3

# Conecta ao banco (ou cria se não existir)
conn = sqlite3.connect('irrigacao.db')
cursor = conn.cursor()

# Criação da tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS sensores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    umidade REAL,
    ph REAL,
    fosforo INTEGER,
    potassio INTEGER,
    bomba INTEGER
)
''')

# Função para inserir dados
def inserir_dados(umidade, ph, fosforo, potassio, bomba):
    cursor.execute('''
    INSERT INTO sensores (umidade, ph, fosforo, potassio, bomba)
    VALUES (?, ?, ?, ?, ?)
    ''', (umidade, ph, fosforo, potassio, bomba))
    conn.commit()

# Função para ler dados
def ler_dados():
    cursor.execute('SELECT * FROM sensores')
    dados = cursor.fetchall()
    for row in dados:
        print(row)

# Função para atualizar dados
def atualizar_dados(id, umidade, ph, fosforo, potassio, bomba):
    cursor.execute('''
    UPDATE sensores
    SET umidade = ?, ph = ?, fosforo = ?, potassio = ?, bomba = ?
    WHERE id = ?
    ''', (umidade, ph, fosforo, potassio, bomba, id))
    conn.commit()

# Função para deletar dados
def deletar_dados(id):
    cursor.execute('DELETE FROM sensores WHERE id = ?', (id,))
    conn.commit()

# EXEMPLOS DE USO:
inserir_dados(25.0, 6.5, 1, 1, 1)
inserir_dados(40.0, 5.9, 0, 1, 0)
ler_dados()

# atualizar_dados(1, 22.0, 6.7, 1, 1, 1)
# deletar_dados(2)

conn.close()
