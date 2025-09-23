def main():
    @bot.message_handler(commands=["start"])
    def start_message(message):

        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("📊 Статистика", callback_data="stats")
        btn2 = types.InlineKeyboardButton("⚙️ Настройки", callback_data="settings")
        btn3 = types.InlineKeyboardButton("ℹ️ Помощь", callback_data="help")

        markup.row(btn1, btn2)
        markup.row(btn3)

        bot.send_message(message.chat.id,messages["START"],reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_handler(call):
            if call.data == "stats":
                bot.answer_callback_query(call.id, "📊 Статистика загружается...")

            elif call.data == "settings":
                bot.answer_callback_query(call.id, "⚙️ Открываю настройки...")

            elif call.data == "help":
                bot.answer_callback_query(call.id, "ℹ️ Раздел помощи")



    @bot.message_handler(commands=["clear"])
    def clear_history(message):
        chat_id = message.chat.id
        message_id = message.message_id

        bot.delete_message(chat_id, message_id)

        try:
            for i in range(message_id, max(1, message_id - 100), -1):
                try:
                    bot.delete_message(chat_id, i)
                except:
                    pass

            bot.send_message(chat_id, "История очищна!")
        except Exception as e:
            bot.send_message(chat_id, f"Ошибка! {e}")


    bot.infinity_polling()


if __name__ == '__main__':
    import telebot
    from telebot import types
    from Funcs import init

    bot, messages, debug = init()

    main()
