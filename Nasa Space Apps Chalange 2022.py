import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from telebot import types

import random
from data import интересные_фото, интересные_текст
from data import polls

bot = telebot.TeleBot('5614252193:AAFjPXntC_9xRF7I9JYChce6qclpcTKc0Dk')
count = 1
choose = 0

answered_polls = {

}

scores = {

}


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(True, True)
    button1 = KeyboardButton('Interesting facts about the telescope 🔭')
    button2 = KeyboardButton('Quiz 🎮')
    button3 = KeyboardButton("Rating🏆")
    keyboard.add(button1, button2)
    keyboard.add(button3)
    bot.send_message(message.chat.id, "Hi " + message.from_user.first_name + " I'm a James Webb space telescope,"
                                                                             " I will inform you about the depths of the bounless space. To "
                                                                             "proceed please select a category",
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Interesting facts about the telescope 🔭")
def info(message):
    global count, интересные_текст, интересные_фото
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="More", callback_data="Ещё факт")
    button2 = InlineKeyboardButton(text="Main", callback_data="Закончить факты")
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_photo(message.chat.id, интересные_фото[count], интересные_текст[count], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "Ещё факт")
def more_info(call):
    global count, интересные_текст, интересные_фото
    count = count + 1
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="More", callback_data="Ещё факт")
    button2 = InlineKeyboardButton(text="Main", callback_data="Закончить факты")
    keyboard.add(button1)
    keyboard.add(button2)
    bot.send_photo(call.message.chat.id, интересные_фото[count], интересные_текст[count], reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Quiz 🎮")
def game(message):
    storage = answered_polls[message.chat.id] if message.chat.id in answered_polls.keys() else []

    i = random.randint(1, len(polls.keys()))
    while i in storage:

        if len(storage) == len(polls):
            return bot.send_message(message.chat.id, "You answered all questions! You are a great fellow!")

        i = random.randint(1, len(polls.keys()))
        print(i)

    storage.append(i)

    poll = polls[i]

    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="First photo", callback_data=f"ANSWER_{i}_1")
    button2 = InlineKeyboardButton(text="Second photo", callback_data=f"ANSWER_{i}_2")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(InlineKeyboardButton(text="Main", callback_data="GO_BACK"))
    bot.send_photo(message.chat.id, poll.photo_url, poll.question, reply_markup=keyboard)

    answered_polls[message.chat.id] = storage


@bot.callback_query_handler(func=lambda call: call.data.startswith('ANSWER_'))
def option_selected(call: types.CallbackQuery):
    data = call.data.split('_')
    id_question = int(data[1])
    option = int(data[2])

    poll = polls[id_question]

    is_correct = True if poll.win_option == option else False
    scores_to_give = 1 if is_correct else -1

    user_scores = scores[call.from_user.id] if call.from_user.id in scores.keys() else 0
    user_scores += scores_to_give
    scores[call.from_user.id] = user_scores

    s = f"You have chosen an answer: {is_correct}. You have {user_scores} points"

    bot.answer_callback_query(call.id, text=s, show_alert=True)
    bot.delete_message(call.message.chat.id, call.message.id)
    game(call.message)


@bot.callback_query_handler(func=lambda call: call.data == "Закончить факты")
def back(call):
    start(call.message)

@bot.callback_query_handler(func=lambda call: call.data == "GO_BACK")
def back_2(call):
    start(call.message)


@bot.message_handler(func=lambda m: m.text == "Rating🏆")
def top_rating(message: types.Message):
    sorted_rating = dict(sorted(scores.items(), key=lambda x: [1]))
    print(sorted_rating)

    s = f"ТОП {len(sorted_rating.keys())} игроков\n\n"

    for user_id, score in sorted_rating.items():
        chat = bot.get_chat(user_id)
        username = chat.username if chat.username is not None else f"{chat.first_name} {chat.last_name}"
        s += f"{username} - {score} очков\n"

    bot.send_message(message.chat.id, s)




bot.polling()