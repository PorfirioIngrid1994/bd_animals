import sqlite3

conn = sqlite3.connect('animais.db')

conn.execute('''CREATE TABLE animais
               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME TEXT NOT NULL,
                PESO_MEDIO REAL NOT NULL,
                COMPRIMENTO_MEDIO REAL NOT NULL,
                NOME_CIENTIFICO TEXT NOT NULL,
                HABITAT TEXT NOT NULL,
                ALIMENTO TEXT NOT NULL,
                RISCO_EXTINCAO TEXT NOT NULL,
                GESTACAO_DIAS INTEGER NOT NULL,
                MEDIA_VIDA_ANOS INTEGER NOT NULL);''')

conn.execute("INSERT INTO animais (NOME, PESO_MEDIO, COMPRIMENTO_MEDIO, NOME_CIENTIFICO, HABITAT, ALIMENTO, RISCO_EXTINCAO, GESTACAO_DIAS, MEDIA_VIDA_ANOS) VALUES ('Texugo', 12, 80, 'Meles meles', 'Floresta', 'Omnívoro', 'Pouco preocupante', 60, 5)")
conn.execute("INSERT INTO animais (NOME, PESO_MEDIO, COMPRIMENTO_MEDIO, NOME_CIENTIFICO, HABITAT, ALIMENTO, RISCO_EXTINCAO, GESTACAO_DIAS, MEDIA_VIDA_ANOS) VALUES ('Panda vermelho', 4, 60, 'Ailurus fulgens', 'Floresta', 'Herbívoro', 'Vulnerável', 135, 14)")
conn.execute("INSERT INTO animais (NOME, PESO_MEDIO, COMPRIMENTO_MEDIO, NOME_CIENTIFICO, HABITAT, ALIMENTO, RISCO_EXTINCAO, GESTACAO_DIAS, MEDIA_VIDA_ANOS) VALUES ('Axolotle', 0.3, 30, 'Ambystoma mexicanum', 'Rio', 'Carnívoro', 'Em perigo', 60, 10)")

cursor = conn.execute("SELECT * FROM animais WHERE HABITAT = 'Floresta'")
for row in cursor:
    print(f"ID: {row[0]}, Nome: {row[1]}, Peso médio: {row[2]}, Comprimento médio: {row[3]}, Nome científico: {row[4]}, Habitat: {row[5]}, Alimento: {row[6]}, Risco de extinção: {row[7]}, Gestação (dias): {row[8]}, Média de vida (anos): {row[9]}")

conn.execute("DELETE FROM animais WHERE ID = 3")

conn.close()
