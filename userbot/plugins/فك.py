import requests
from telebot import types
import telebot
from time import sleep
import random
token = '1969136232:AAHgawyn8HVQnVeo0PoqsXio_VCvy-GVoa4'
bot = telebot.TeleBot(token)
r=requests.session() 
co = types.InlineKeyboardButton(text ="جلب صفحة عشوائية",callback_data = 'check')
#----#


@bot.message_handler(commands=['start'])
def start(message):
    use = message.from_user.username
    fr = message.from_user.first_name
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co)
    bjj = message.chat.id
    bot.send_message(message.chat.id,text=f"""<strong>
عزيزي <code>{fr}</code>, 
- - - - - - - - - - 
اهلا بك في بوت القرآن

يمكنك أن تجلب صفحة عشوائية من القرآن الكريم وقرائَتها

نصيحة حسن : كل يوم اقرالك 3 صفحات تاخذ منك 5 دقايق وهم تاخذ ثواب
- - - - - - - - - - 
المطور  : @HASONI_LQ
</strong>
    """,parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call: True)
def qwere(call):
    if call.data == 'check':
    	combo(call.message)   	
def combo(message):
		bot.send_message(message.chat.id,"<strong>يتم العثور الرجاء الانتظار... </strong>",parse_mode="html")
		rl = random.randint(1,600)
		url = f"https://iuytiuyt.000webhostapp.com/newquran/{rl}.gif"
		bot.send_photo(message.chat.id,url,caption=f"<strong>تم جلب صفحة عشوائية \nرقم الصفحة {rl}</strong>",parse_mode="html")
		bot.send_message(message.chat.id,"<strong>ادعي لـحسن</strong>",parse_mode="html") 
		
    
pass
#داشوفك تريد تخمط
bot.polling(True)
