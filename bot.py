import calendar
import telebot
token='5757326634:AAELHxo58JWEojas741wIBEEwYzNsZKa7AU'
bot = telebot.TeleBot(token)

list1=['Сист. программирование', 'Архитектура', 'Прикл. программирование', '']
list2=['Инф. сист. и сети/Web-мастеринг', 'Физ-ра', 'Web-мастеринг','']
list3=['Сист. программирование', 'Прикл. программирование', 'Осн. постр. АС','']
list4=['Офисное пр.', 'Осн. постр. АС', 'БЖ/Архитектура','ИН.яз']
list5=['Инф. сист. и сети', 'Web-мастеринг', 'Офисное пр.','']
list6=['Web-мастеринг', 'БЖ', '','']

dict={0: list1, 1: list2, 2: list3,
      3:list4, 4: list5, 5: list6}

@bot.message_handler(commands=['start'])
def repeat_all_message(message):
    bot.send_message(message.chat.id, 'Дата:')

@bot.message_handler(content_types=["text"])
def data(message):
    list=message.text.split('.')
    try:
        date=calendar.weekday(int(list[2]), int(list[1]), int(list[0]))
        bot.send_message(message.chat.id, dict[date][0] +'\n' + dict[date][1]+
                         '\n'+dict[date][2]+'\n'+dict[date][3])
    except:
        bot.send_message(message.chat.id, 'Неверные данные')

if __name__ == '__main__':
  bot.polling(none_stop=True)

