import yaml

def load():
    with open('config.yaml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    bot = config["bot"]["token"]

    if bot == "your_bot_token" or bot == "":
        print("⚠️ ВНИМАНИЕ: Введите токен бота в конфиге!")
        exit()

    return config