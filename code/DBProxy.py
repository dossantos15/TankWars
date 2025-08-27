import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3. connect(db_name)
        self.connection.execute('''
                                    CREATE TABLE IF NOT EXISTS dados(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    ponto INTEGER NOT NULL,
                                    date TEXT NOT NULL)
                                '''
                                )

    def save(self, ponto_dict: dict):
        self.connection.execute('INSERT INTO dados (name, ponto, date) VALUES (:name, :ponto, :date)', ponto_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY ponto DESC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()