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

Здесь оказывают услуги розыгрыша, которые запоминаются надолго. 

🔹 Насолила какая-то личность👤? 
🔹 Вымогатель достал💸? 
🔹 Или просто хочешь prank-нуть друга🤡?

Тогда тебе точно к нам.

🎯 ТОЛЬКО У НАС ты можешь заказать:
• Докс 📁
• Сваттинг 👮  
• Спам-атаку 💥
• Удаление аккаунтов 🗑️
• И многое другое...

✅ ПОЧЕМУ МЫ?
▪️ Качественно
▪️ Дешево* *
▪️ Полная анонимность

Покупай, решим твою "проблему". 😉''',
                'MENU_BUTTON_1': '🔧 Поддержка',
                'MENU_BUTTON_2': '⚙️ Профиль',
                'MENU_BUTTON_3': '🎀 Заказ',
                'MENU_BUTTON_4': 'ℹ Вопросы',
                'PRICES': '''Расценки:
                
Расценки:
Roblox (робукс) x1 ≈ $0.0127 (1$ ≈ 78)
Standoff (голдi) x1 ≈ $0.006 (1$ ≈ 166G)
Russia (Рубль) 1$ ≈ 83.75 ₽
Бутан (Нгултрум): 1$ ≈ 83.75 BTN
Сейшельские острова (Сейшельская рупия): 1$ ≈ 13.50 SCR
Венесуэла (Венесуэльский боливар): 1$ ≈ 3,500,000 VES
                
• Докс — 2.45 $
• Сваттинг — 12.50 $
• Спам-атака — 0.99 $
• Снос акка — 4.5 $
• Поджог двери — 63.33 $
''',
                'EXIT_BUTTON': '⏪ Назад',
                'ORDER_BUTTON': '👛 Сделать заказ',
                'DEPOSIT_BUTTON': '💸 Пополнить баланс',
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