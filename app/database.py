from sqlite3 import connect, Error
from sqlite3.dbapi2 import Connection
from queue import Queue
from sys import exit

"""
CREATE TABLE captcha_discord(
    id INTEGER PRIMARY KEY,
    verification_captcha VARCHAR(10),
    id_user VARCHAR(18)
)
"""


def get_connection() -> Connection:
    try:
        return connect("./app/sql/database.db")
    except Error as e:
        print(e)
        exit()


def insert_data(text: str, id: int) -> None:
    sql = """INSERT OR REPLACE INTO captcha_discord(verification_captcha,id_user)
    VALUES(?1,?2); """
    conn = get_connection()
    cursor=conn.cursor()
    cursor.execute(sql, (text, str(id),))
    conn.commit()
    


def selecting_data(text: str, id: int,queue:Queue[str]):
    sql = "SELECT id_user FROM captcha_discord WHERE verification_captcha =?1 AND id_user=?2"
    conn = get_connection()
    queue.put( conn.cursor().execute(sql, (text, str(id),)).fetchone())




def delete_data(id: int) -> None:
    sql = "DELETE FROM  captcha_discord WHERE id_user=?1"
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql, (str(id),))
    conn.commit()
