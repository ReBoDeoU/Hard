import requests

bot = "1970139230:AAHbU9GIVoXyS33ykvgrskZK1Asj080_TQ0"


@bot.message_handler(commands=['get'])
def telegra(message):
    token = 'token'
    country = 'bangladesh'
    operator = 'any'
    product = 'telegram'

    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }

    response1 = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headers).json()
    forid = response1['id']
    bot.send_message(message.chat.id,response1['phone'])
    while True:
        response2 = requests.get('https://5sim.net/v1/user/check/' + str(forid), headers=headers).json()['sms']
        if response2 != []:
            bot.send_message(message.chat.id,f"{response2[0]['text']}")
            break
bot.polling(True,timeout=3423)
