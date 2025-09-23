path = "config.yaml"
def setup():
    import yaml

    config = {
        'bot': {
            'token': 'your_bot_token',
        },
        'settings': {
            'debug': False,
            'language': 'ru'
        },
        'messages': {
            'ru': {
                'START': '''😈 Добро пожаловать в магазин "Тихонечко". 

Здесь оказывают *услуги розыгрыша*, которые запоминаются надолго. 

🔹 Насолила какая-то личность👤? 
🔹 Вымогатель достал💸? 
🔹 Или просто хочешь prank-нуть друга🤡?

*Тогда тебе точно к нам.*

🎯 ТОЛЬКО У НАС ты можешь заказать:
• *Докс* 📁
• *Сваттинг* 👮♂️  
• *Спам-атаку* 💥
• *Удаление аккаунтов* 🗑️
• *И многое другое...*

✅ *ПОЧЕМУ МЫ?*
▪️ *Качественно*
▪️ *Дешево* 
▪️ *Полная анонимность*

*Покупай, решим твою "проблему".* 😉''',
                'START_BUTTON_1': '📊 Статистика',
                'START_BUTTON_2': '📊 Ст2ка',
                'START_BUTTON_3': '📊 Ст4ка'
            }
        }
    }

    from os import path
    from bot_token import bot_token
    if path.exists(r"../bot_token.py"):
        config["bot"]["token"] = bot_token()

    if __name__ == '__main__':
        path = "../config.yaml"
    with open(path, 'w', encoding='utf-8') as file:
        yaml.dump(config, file, default_flow_style=False, allow_unicode=True)

    print("Config Created")
    print("Введите токен бота в конфиге")


    exit()

if __name__ == '__main__':
    setup()