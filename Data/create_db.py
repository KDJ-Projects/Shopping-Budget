import sqlite3 as sq3
from sqlite3 import Error


class CreatDB:
    def __init__(self) -> None:
        self.result = print("Connection is astablisched: Database is created")
        self.conn = sq3.connect("./Data/acouting.db")
        self.cursor_obj = self.conn.cursor()

    def sql_connection(self):
        try:
            self.conn
            return self.conn, self.result
        except Error:
            print(Error)

    def sql_table(self):
        self.conn
        self.cursor_obj
        self.cursor_obj.execute(
            "CREATE TABLE IF NOT EXISTS uitgaven(Datum date, Bedrag real, Winkel text);"
        )
        self.conn.commit()
        self.conn.close()


if __name__ == "__main__":
    CreatDB().sql_connection()
    CreatDB().sql_table()