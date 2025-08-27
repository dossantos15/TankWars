import sqlite3


class DBProxy:
    def __init__(self, db_nome: str):
        self.db_nome = db_nome
        self.connection = sqlite3. connect(db_nome)
        self.connection.execute('''
                                    CREATE TABLE IF NOT EXISTS dados(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    ponto INTEGER NOT NULL,
                                    data TEXT NOT NULL)
                                '''
                                )

    def save(self, ponto_dict: dict):
        self.connection.execute('INSERT INTO dados (nome, ponto, data) VALUES (:nome, :ponto, :data)', ponto_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY ponto DESC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()
