import bs4
import parser

#main variables
TOKEN = "555555555:AAAAaaaAaaA1a1aA1AAAAAAaaAAaa4AA"
bot = telebot.TeleBot(TOKEN)

#handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, '������, ����� � �������, � ���� ������� ��������� � �����')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "������":
        bot.send_message(chat_id, '������, � ��� - ������ �����.')
    elif text == "��� ����?":
        bot.send_message(chat_id, '������, � � ����?')
    else:
        bot.send_message(chat_id, '��������, � ��� �� ����� :(')

bot.polling()