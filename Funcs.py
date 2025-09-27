from os import path
from telebot import types
import telebot

import sqlite3

def init():
    from config.load import load

    if not path.exists("config.yaml"):
        from config.setup import setup
        setup()

    config = load()

    database_data = config["settings"]["database"]

    messages = config["messages"]["ru"]
    bot = config["bot"]["token"]
    bot = telebot.TeleBot(bot)

    database = (database_data["users"]["database-name"], database_data["users"]["database-table-name"])

    print("Bot enabled")

    return bot, messages, database


def db_create(db_name, db_table):
    with sqlite3.connect(str(db_name) + '.db') as db:
        cursor = db.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {db_table} (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
balance REAL NOT NULL,
last_message_id INTEGER)''')



def db_insert(db_name, db_table, id, username, balance):
    with sqlite3.connect(str(db_name) + '.db') as db:
        cursor = db.cursor()

        cursor.execute(f'''INSERT INTO {db_table} (id, username, balance) VALUES (?, ?, ?)''',
                       (id, username, balance))

def db_update(db_name, db_table):
    with sqlite3.connect(str(db_name) + '.db') as db:
        cursor = db.cursor()

        cursor.execute(f'''UPDATE {db_table} SET age = ? WHERE username = ?''', (29, 'newuser'))

def db_delete(db_name, db_table):
    with sqlite3.connect(str(db_name) + '.db') as db:
        cursor = db.cursor()

        cursor.execute(f'''DELETE FROM {db_table} WHERE username = ?''', ('newuser'))

def db_select(db_name, db_table, *where, how_many=None):
    with sqlite3.connect(str(db_name) + '.db') as db:
        cursor = db.cursor()

        if len(where) != 0:
            cursor.execute(f'''SELECT * FROM {db_table} WHERE {where[0]} = ?''', (where[1],))
            return cursor.fetchone()

        if how_many is not None:
            cursor.execute(f'''SELECT * FROM {db_table}''')
            return cursor.fetchmany(how_many)

        cursor.execute(F'''SELECT * FROM {db_table}''')
        return cursor.fetchall()

def db_new_user(db_name, db_table, id, username):
    user = db_select(db_name, db_table, 'id', id)
    if user is None:
        print("✅ Обнаружен новый пользователь. Добавление в базу данных...")
        db_insert(db_name, db_table, id, username, 0.0)
        print(f"✅ Пользователь {username} успешно добавлен в базу данных.")
        return
    else:
        return

def db_show_user_profile(db_name, db_table, id):
    print(123)

def db_delete_user_profile(db_name, db_table):
    ...



# db_name = 'database'
# db_table = 'Users'
# db_create(db_name, db_table)

# # Правильный вызов SELECT с WHERE
# a = db_select(db_name, db_table, 'id', 1)
# print(a)
#
# # Получаем все данные
# all_data = db_select(db_name, db_table)
# print("All data:", all_data)