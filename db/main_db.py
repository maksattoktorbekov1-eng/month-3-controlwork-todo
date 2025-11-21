import sqlite3
from config import path_db
from db import queries

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_LIST)
    conn.commit()
    conn.close()
    print("База данных подключена!")

def add_item(item):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.ADD_ITEM, (item,))
    conn.commit()
    conn.close()

def get_items():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.GET_ITEMS)
    items = cursor.fetchall()
    conn.close()
    return items

def update_item(item_id, completed):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_ITEM, (completed, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_ITEM, (item_id,))
    conn.commit()
    conn.close()
