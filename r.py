import os
import time
import requests
import random
import string
import requests
import telebot
from telebot import *
from telebot import util
from telebot import types

tokin = '5207013751:AAHhqW8JMrCKjGhOrV5M5VIFPY5f6cR3ZAw'
tok = input('Token : ')
def check_user(user_id):
  global tokin, Channel
  request = requests.get(f"https://api.telegram.org/bot{tokin}/getChatMember?chat_id=@aauua&user_id={user_id}").text
  if '"status":"left"' in request or '"Bad Request: USER_ID_INVALID"' in request or '"status":"kicked"' in request or 'user not found' in request:
    return False
  else:
    return True

def random_user(name):
    char='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    namber = " ".join(str(1234567890)) 
    while True:
        randomUser = []
        charA = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        charC = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        charB = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        if name == "User-3":
            randomUser.append(random.choice(char) + "_" + random.choice(char) + "_" + random.choice(char))
            randomUser.append(charA + "_" + charB + "_" + charB)
            randomUser.append(charB + "_" + charA + "_" + charB)
            randomUser.append(charB + "_" + charB + "_" + charA)
            randomUser.append(charB + "_" + charA + "_" + charA)
            randomUser.append(charA + "_" + charB + "_" + charA)
            randomUser.append(charA + "_" + charA + "_" + charB)
        elif name == "4":
            randomUser.append(random.choice(char) + random.choice(char) + random.choice(char))
            randomUser.append(charA + charB + charB + charB)
            randomUser.append(charB + charA + charB + charB)
            randomUser.append(charB + charB + charA + charB)
            randomUser.append(charB + charA + charA + charB)
            randomUser.append(charA + charB + charA + charB)
            randomUser.append(charA + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA)
            randomUser.append(charB + charA + charB + charA)
            randomUser.append(charB + charB + charA + charA)
            randomUser.append(charB + charA + charA + charA)
            randomUser.append(charA + charB + charA + charA)
            randomUser.append(charA + charA + charB + charA)
        elif name == "User-4":
            randomUser.append(random.choice(char) + "_" + random.choice(char) + "_" + random.choice(char))
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + charB + charA + charA + charB + charB)
            randomUser.append(charA + "_" + charA + "_" + charB + "_" + charA)
        elif name == "User-5":
            randomUser.append(random.choice(char) + "_" + random.choice(char) + "_" + random.choice(char))
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
            randomUser.append(charA + charB + charC + 'BoT')
        elif name == "5":
            randomUser.append(random.choice(char) + random.choice(char) + random.choice(char) + random.choice(char) + random.choice(char))
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)
            randomUser.append(charA + charB + charB + charA + charB + charB)

        User = random.choice(randomUser)
        if str(User[0]) in namber or len(User) < 5:
            continue
        else:
            return User
            break

bot = telebot.TeleBot(tok)
@bot.message_handler(commands=['start'])
def welcome(message):
    channel = types.InlineKeyboardButton(text=" ⚒️ Channel Developer ", url="https://t.me/aauua")
    if check_user(message.from_user.id):
        start = types.InlineKeyboardButton(text=" 📮 Start ", callback_data="start")
        programmer = types.InlineKeyboardButton(text=" 👨🏻‍💻 Developer ", url="https://t.me/HvvHH")
        Keyboards = types.InlineKeyboardMarkup()
        Keyboards.row_width = 2
        Keyboards.add(start,  programmer,  channel)
        bot.send_message((message.chat.id), text=f"🌹| Hi {message.from_user.first_name} in Bot Check Uesr Telegram \n🔰| Please Click", reply_to_message_id=(message.message_id), reply_markup=Keyboards)
    else:
        Keyboard = types.InlineKeyboardMarkup()
        Keyboard.row_width = 1
        Keyboard.add(channel)
        bot.reply_to(message, text=f"💖| Hi {message.from_user.first_name} \n🔰| You must subscribe to the developer's channel Then press /start", reply_markup=Keyboard)
        
@bot.callback_query_handler(func=lambda call: True)
def bot_query_handler(call):
    if call.data == "start":
        start(call.message)
    elif call.data == "User-3":
        run(call.message, "User-3")
    elif call.data == "User-4":
        run(call.message, "User-4")
    elif call.data == "User-5":
        run(call.message, "User-5")

def start(message):
    Button1 = types.InlineKeyboardButton(text=" ✲ @X11X11 ", callback_data="User-3")
    Button9 = types.InlineKeyboardButton(text=" ✲ @X-1BoT ", callback_data="User-5")
    Button2 = types.InlineKeyboardButton(text=" ✲ @X1XX11", callback_data="User-4")
    Key = types.InlineKeyboardMarkup()
    Key.row_width = 1
    Key.add(Button1, Button2, Button9)
    bot.edit_message_text(text=f'🔰| Please Click', chat_id=int(message.chat.id), message_id=message.message_id, reply_markup=Key)

def run(message, name):
    messages = bot.send_message((message.chat.id), f'📮 Starting ⏳ Please Wait ...')
    time_imog = list("⌛⏳⌛⏳⌛⏳⌛")
    for i in range(len(time_imog)):
        bot.edit_message_text(text=f'📮| Starting {time_imog[i]} Please Wait ...', chat_id=int(message.chat.id), message_id=messages.message_id)
        time.sleep(0.6)
    n = 0
    sleep = 1.1
    c = 100
    Error = ""
    loading = 0
    Count_Done = 0
    Count_Error = 0
    Count_group = 0
    Count_person = 0
    Count_channel = 0
    time_start = time.time()
    while n < c:
        loading = int((int(n) / int(c)) * 100)
        user = random_user(name)
        response = requests.get(f"https://t.me/{user}").text
        if response.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            Count_Done += 1
            bot.edit_message_text(text=f"""◆━━━━━◆ ✲ ◆━━━━━◆
✅| User Telegram None
◆━━━━━◆ ✲ ◆━━━━━◆
🔢| user : @{user}
◆━━━━━◆ ✲ ◆━━━━━◆
📦| Count User None : {Count_Done}
◆━━━━━◆ ✲ ◆━━━━━◆
⛔| Count person : {Count_person}
⛔| Count channel : {Count_channel}
⛔| Count group : {Count_group}
◆━━━━━◆ ✲ ◆━━━━━◆
📛| Count User All Error : {Count_Error}
◆━━━━━◆ ✲ ◆━━━━━◆
⏳| Elapsed time : {str(int(time.time() - time_start))} S
⚡| Loading : {loading}%
⌛| Time End : {str(int(sleep * c))} S
◆━━━━━◆ ✲ ◆━━━━━◆
👨🏻‍💻| Developer : @HvvHH
⚒️| Channel : @aauua
◆━━━━━◆ ✲ ◆━━━━━◆""", chat_id=int(message.chat.id), message_id=messages.message_id)
            bot.send_message(message.chat.id, f"""
            - New Hit baby
            - x - x - x - x -
            - @{user}
            - x - x - x - x -
            Develpoers: @HvvHH""")
        else:
            Count_Error += 1
            if response.find('subscribers') >= 0:
                Error = "channel"
                Count_channel += 1
            elif response.find('members') >= 0:
                Error = "group"
                Count_group += 1
            else:
                Error = "person"
                Count_person += 1
            bot.edit_message_text(text=f"""◆━━━━━◆ ✲ ◆━━━━━◆
❌| User Telegram {Error}
◆━━━━━◆ ✲ ◆━━━━━◆
🔢| User : @{user} 
◆━━━━━◆ ✲ ◆━━━━━◆
📦| Count User Success : {Count_Done}
◆━━━━━◆ ✲ ◆━━━━━◆
⛔| Count person : {Count_person}
⛔| Count channel : {Count_channel}
⛔| Count group : {Count_group}
◆━━━━━◆ ✲ ◆━━━━━◆
📛| Count All User Error : {Count_Error}
◆━━━━━◆ ✲ ◆━━━━━◆
⏳| Elapsed time : {str(int(time.time() - time_start))} S
⚡| Loading : {loading}%
⌛| Time End : {str(int(sleep * c))} S
◆━━━━━◆ ✲ ◆━━━━━◆
⚡| Loading : {loading}%
◆━━━━━◆ ✲ ◆━━━━━◆
👨🏻‍💻| Developer : @HvvHH
⚒️| Channel : @aauua
◆━━━━━◆ ✲ ◆━━━━━◆""", chat_id=int(message.chat.id), message_id=messages.message_id)
        time.sleep(sleep)
        n += 1
        loading = int((int(n) / int(c)) * 100)

while True:
    try:
        print("Done")
        bot.polling(True)
        break
    except Exception as ex:
        print(f"Error polling : {ex}")
        telebot.logger.error(ex)
        continue
