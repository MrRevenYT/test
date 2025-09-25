from os import path
from telebot import types
import telebot

import sqlite3

def init():
    from config.load import load

    if not path.exists("config.yaml"):
        from config.setup import setup
        setup()

    bot, messages, debug = load()

    bot = telebot.TeleBot(bot)

    print("Bot enabled")

    return bot, messages, debug


def db_create(db_name, db_table):
    with sqlite3.connect(str(db_name) + '.db') as db:
        cursor = db.cursor()

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {db_table} (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
balance REAL NOT NULL)''')

def db_insert(db_name, db_table):
    with sqlite3.connect(str(db_name) + '.db') as db:
        cursor = db.cursor()

        cursor.execute(f'''INSERT INTO {db_table} (id, username, balance)
''')

db_name = 'database'
db_table = 'Users'
db_create(db_name, db_table)
