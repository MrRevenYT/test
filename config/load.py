import yaml

def load():
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    bot = config["bot"]["token"]
    messages = config["messages"]["ru"]


    debug = config["settings"]["debug"]

    if bot == "your_bot_token" or bot == "":
        print("Ошибка! Введите токен бота в конфиге")
        exit()

    return bot, messages, debug