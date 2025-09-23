from os import path
import telebot

def init():
    from config.load import load

    if not path.exists("config.yaml"):
        from config.setup import setup
        setup()

    bot, messages, debug = load()

    bot = telebot.TeleBot(bot)

    print("Bot enabled")

    return bot, messages, debug
