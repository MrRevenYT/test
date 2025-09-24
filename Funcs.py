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


def db_create(db_name):
    with sqlite3.connect(str(db_name) + '.db') as db:
        cursor = db.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
balance REAL NOT NULL)''')

db_name = 'users'
db_create(db_name)