import yaml
from os import path

def setup():
    config = {
        'bot': {
            'token': 'your_bot_token',
            'admins': [8099756119],
            'supports': []
        },
        'settings': {
            'debug': False,
            'database': {
                'users': {
                    'database-name': 'database',
                    'database-table-name': 'Users'
                }
            }
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
▪️ Дешево
▪️ Полная анонимность

Покупай, решим твою "проблему". 😉''',
                'MENU_BUTTON_1': '🔧 Поддержка',
                'MENU_BUTTON_2': '⚙️ Профиль',
                'MENU_BUTTON_3': '🎀 Заказать',
                'MENU_BUTTON_4': 'ℹ Вопросы',
                'PROFILE_BUTTON_1': '❌ Удалить данные',
                'PROFILE_BUTTON_2': '💸 Пополнить баланс',
                'EXIT_BUTTON': '⏪ Назад',
                'ORDER_BUTTON': '🎀 Сделать заказать',
                'PRICES': '''Расценки:
                
Обмен:
Roblox (робукс) x1 ≈ $0.0127 (1$ ≈ 78 р)
Standoff (голдi) x1 ≈ $0.006 (1$ ≈ 166 G)
Hamster (коiн) x1 ≈ $0,0000000003 (1$ ≈ 2968472447 HAM)

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
            }
        }
    }

    config_path = "config.yaml"
    if __name__ == '__main__':
        config_path = "../config.yaml"

    try:
        if path.exists("bot_token.py") or path.exists("../bot_token.py"):
            from bot_token import bot_token
            token = bot_token()
            config["bot"]["token"] = token

    except ImportError:
        print("⚠️ Файл bot_token.py не найден")

    try:
        with open(config_path, 'w', encoding='utf-8') as file:
            yaml.dump(config, file, default_flow_style=False, allow_unicode=True, indent=2)

        print("✅ Конфиг был успешно загружен!")
        print("✅ Config path:", path.abspath(config_path))

        if config["bot"]["token"] == 'your_bot_token_here':
            print("⚠️ ВНИМАНИЕ: Не забудьте ввести токен бота в config.yaml")
            exit()
        else:
            print("✅ Токен бота был успешно загружен из bot_token.py")

    except Exception as e:
        print(f"❌ Ошибка при создании config.yaml: {e}")

if __name__ == '__main__':
    setup()