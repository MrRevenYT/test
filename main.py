def main():

    @bot.message_handler(commands=["start"])
    def start_message(message=None, call=None):

        if message:
            chat_id = message.chat.id
        elif call:
            chat_id = call.message.chat.id
        else:
            return

        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton(messages["MENU_BUTTON_1"], callback_data="stats")
        btn2 = types.InlineKeyboardButton(messages["MENU_BUTTON_2"], callback_data="settings")
        btn3 = types.InlineKeyboardButton(messages["MENU_BUTTON_3"], callback_data="order")
        btn4 = types.InlineKeyboardButton(messages["MENU_BUTTON_4"], callback_data="help")

        markup.row(btn1, btn2, btn3)
        markup.row(btn4)

        if call:
            try:
                bot.edit_message_text(call.message.message.id ,chat_id, messages["START"], reply_markup=markup)
            except:
                bot.send_message(chat_id, messages["START"], reply_markup=markup)
        else:
            bot.send_message(chat_id, messages["START"], reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):

        if call.data == "exit":
            bot.answer_callback_query(call.id, "Выход...")
            start_message(call=call)

        elif call.data == "profile":
            bot.answer_callback_query(call.id, "Загрузка профиля...")

        elif call.data == "order":
            bot.answer_callback_query(call.id, "Загрузка заказа...")
            time.sleep(randint(3, 5))

            markup = types.InlineKeyboardMarkup()

            btn1 = types.InlineKeyboardButton(messages["ORDER_BUTTON_1"], callback_data="exit")
            btn2 = types.InlineKeyboardButton(messages["ORDER_BUTTON_2"], callback_data="order_2")

            markup.row(btn1)
            markup.row(btn2)

            bot.send_message(call.message.chat.id, messages["PRICES"], reply_markup=markup)




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
    from random import randint
    import time
    import telebot
    from telebot import types
    from Funcs import init


    bot, messages, debug = init()

    main()
