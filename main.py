def main():

    @bot.message_handler(commands=["start"])
    def start_message(message=None, call=None):

        if message:
            chat_id = message.chat.id
            user_id = message.from_user.id
            user_username = message.from_user.username

            db_new_user(database[0], database[1], user_id, user_username)

        elif call:
            chat_id = call.message.chat.id
        else:
            return

        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton(messages["MENU_BUTTON_1"], callback_data="stats")
        btn2 = types.InlineKeyboardButton(messages["MENU_BUTTON_2"], callback_data="profile")
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

    @bot.message_handler(commands=["profile"])
    def show_profile(message=None, call=None):

        if message:
            chat_id = message.chat.id
            user_id = message.from_user.id
            user_username = message.from_user.username

        elif call:
            chat_id = call.message.chat.id
            user_id = call.message.from_user.id
        else:
            return

        print(chat_id)

        db_show_user_profile(database[0], database[1], user_id)

        markup = types.InlineKeyboardMarkup()

        markup.row(types.InlineKeyboardButton(messages["PROFILE_BUTTON_1"], callback_data="deposit"))
        markup.row(types.InlineKeyboardButton(messages["PROFILE_BUTTON_2"], callback_data="delete_account"))
        markup.row(types.InlineKeyboardButton(messages["EXIT_BUTTON"], callback_data="exit"))


        bot.send_message(chat_id, '123', reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):

        if call.data == "exit":
            bot.answer_callback_query(call.id, "Выход...")
            time.sleep(round(uniform(1.4, 3.5), 3))

            start_message(call=call)

        elif call.data == "profile":
            bot.answer_callback_query(call.id, "Загрузка профиля...")
            time.sleep(round(uniform(1.4, 3.5), 3))
            show_profile(call=call)

        elif call.data == "order":
            bot.answer_callback_query(call.id, "Загрузка заказа...")
            time.sleep(round(uniform(1.4, 3.5), 3))

            markup = types.InlineKeyboardMarkup()

            btn1 = types.InlineKeyboardButton(messages["EXIT_BUTTON"], callback_data="exit")
            btn2 = types.InlineKeyboardButton(messages["ORDER_BUTTON"], callback_data="order_2")

            markup.row(btn1)
            markup.row(btn2)

            bot.send_message(call.message.chat.id, messages["PRICES"], reply_markup=markup)



    @bot.message_handler(commands=["info"])
    def last_message_info(message):
        chat_id = message.chat.id
        message_id = message.id

        print(chat_id, "\n", message_id)

        bot.delete_message(chat_id, message_id)

        chat_id = message.chat.id
        message_id = message.id

        print(chat_id, "\n", message_id)

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


    bot.infinity_polling(timeout=10,long_polling_timeout=5,restart_on_change=False)


if __name__ == '__main__':
    from random import uniform
    import time
    from telebot import types
    from Funcs import init, db_new_user, db_show_user_profile

    bot, messages, database = init()



    main()
