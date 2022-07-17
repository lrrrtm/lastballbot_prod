import sqlite3
from PIL import Image, ImageDraw, ImageFont
import telebot
import re
import random
import qrcode
from constants import *
import string
from buttons import *

bot = telebot.TeleBot(api)
db = sqlite3.connect(database, check_same_thread=False)
cur = db.cursor()

cur.execute("select firstname, lastname, tID, ticketType, transferType from mainTable")
data = cur.fetchall()

#data = [["Артём", "Ларионенко", 409801981, 0, 3]]
for a in data:
    try:
            firstname, lastname, tID, ticketType, transferType = a[0], a[1], a[2], a[3], a[4]

            bot.send_message(tID, "Господа, вот и всё. "
                                   "\n\nПрошло последнее событие, которое поставило для нашего выпуска точку в нашей большой книге под названием «Гимназия №40». Мы больше не господа гимназисты, а будущие студентами университетов, которые разбросаны по всему миру."
                                   "\n\nМы хотим поблагодарить Вас за всё. С кем-то мы вместе росли на протяжении всех 11 лет, с кем-то стали знакомы совсем недавно, но, несмотря ни на что, мы ценим каждый момент, который мы провели вместе. Благодаря вам гимназия для нас стала местом, в которое хотелось возвращаться снова и снова. Было множество моментов, наполненных как и печальными эмоциями, так и позитивными и мы рады, что помимо слез, стресса, нервов и страха в наших жизнях были вы - друзья, которые поддерживали на каждом сложном моменте и не давали нам сойти с ума. "
                                   "\n\nМы хотим пожелать вам не терять мотивацию и оставаться такими же замечательными и целеустремленными людьми, мечтающим о чём-то большом, грандиозном, что сможет изменить нашу страну и мир только в лучшую сторону. "
                                   "\nМы в вас верим, друзья. У вас все получится."
                                   "\n\nСпасибо за всё и с любовью ваши,"
                                   "\nИлья Болгов, Сева Воропаев, Ваня Мофа, Данилка Птичкин и Лиза Лазарева")
            bot.send_video(tID, open(f"{rootSource}/result.mp4", "rb"), width=2160, height=3840)
            print(tID, firstname, lastname, "ОТПРАВЛЕНО")

    except Exception as e:
        bot.send_message(409801981, f"{a[0], a[1], a[2]}\nНе удалось отправить сообщение\nОшибка: {str(e)}")