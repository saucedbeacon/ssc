import requests
import time
from datetime import datetime
import telebot

bot = telebot.TeleBot("6957326767:AAGiZdU1oAv8kmKkyYe-3V30lN4-XyoBalU", parse_mode=None)
tries = []
headers = {
  'authority': 'api.solscan.io',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'if-none-match': 'W/"1bcf-HaL4Qv7RM97xd6iPTHffMiOgD8c"',
  'origin': 'https://solscan.io',
  'referer': 'https://solscan.io/',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'Cookie': '__cf_bm=F8XgTiksnmD4.XUrUnBy0nx..wLkGF3TFSCbXfoAN.g-1703330729-1-AUkCjU/sNNa16Uhy6OvePhh8+iuuz7IpmJ4dmBsfMhHdVo2dZD+smsku6fQKlesxJGVKFU6deq0mGvQD/z+T/1U='
}

while False:
    orderbookLastTx = requests.get("https://api.solscan.io/v2/account/transaction?address=srmqPvymJeFKQ4zGQed1GFppgkRHL9kaELCbyksJtPX&limit=50&cluster=", headers=headers).json()
    for i in orderbookLastTx['data']:
        if i['status'] != 'Fail':
            for t in i["parsedInstruction"]:
                if t['type'] == 'initializeMarket':
                    txHash = i['txHash']
                    tokenQuote = t['params']['quoteMint']
                    baseQuote = t['params']['baseMint']
                    tokenQuoteInfo = requests.get('https://api.solscan.io/v2/token/meta?token='+tokenQuote, headers=headers).json()
                    tokenQuoteSymbol = tokenQuoteInfo['data']['symbol']
                    tokenQuoteIcon = tokenQuoteInfo['data']['icon']
                    tokenQuoteName = tokenQuoteInfo['data']['name']
                    birdEyeLink = "https://birdeye.so/token/"+tokenQuote
                    if baseQuote == 'So11111111111111111111111111111111111111112':
                        baseQuoteName = "SOL"
                    else:
                        baseQuote = baseQuoteName
while True:
    try:
        while True:
            orderbookLastTx = requests.get("https://api.solscan.io/v2/account/transaction?address=5Q544fKrFoe6tsEbD7S8EmxGTJYAKtTVhAW5Q5pge4j1&limit=999&cluster=", headers=headers).json()
            for i in orderbookLastTx['data']:
                if i['status'] != 'Fail':
                    for t in i["parsedInstruction"]:
                        if t['type'].lower() == 'raydium:purchase':
                            if True:
                                print(i['txHash'])
                                button_solscan = telebot.types.InlineKeyboardButton('Solscan', url="https://solscan.io/tx/"+i["txHash"])
                                keyboard = telebot.types.InlineKeyboardMarkup()
                                keyboard.add(button_solscan)
                                constructStr = f"""
*Found Tx Signature of InitializeMarket - Raydium*

Transaction Hash : `{i['txHash']}`
"""
                                bot.send_message(-1002110518878, constructStr, parse_mode='markdown', reply_markup=keyboard)
                                txHash = i['txHash']
                                while True:
                                    try:
                                        txnInfo = requests.get('https://api.solscan.io/v2/transaction?tx='+txHash, headers=headers).json()
                                        for k in list(txnInfo['data']['parsedInstruction']):
                                            if k['type'] == 'purchase':
                                                currentTime = datetime.fromtimestamp(txnInfo["data"]["blockTime"], tz=None)
                                                tokenQuote = k['params']['userIdoInfo']
                                                tokenQuoteC = tokenQuote
                                                baseQuote = k['params']['userOwner']
                                                if baseQuote != 'So11111111111111111111111111111111111111112':
                                                    tokenQuote = baseQuote
                                                    baseQuote = tokenQuoteC                                                
                                                tokenQuoteInfo = requests.get('https://api.solscan.io/v2/token/meta?token='+tokenQuote, headers=headers).json()
                                                tokenQuoteSymbol = tokenQuoteInfo['data']['symbol']
                                                try:
                                                    tokenQuoteIcon = tokenQuoteInfo['data']['icon']
                                                except:
                                                    tokenQuoteIcon = None
                                                tokenQuoteName = tokenQuoteInfo['data']['name']
                                                birdEyeLink = "https://birdeye.so/token/"+tokenQuote
                                                bonkBotLink = 'https://t.me/neo_bonkbot?start=ref_m8gai_ca_'+tokenQuote
                                                if baseQuote == 'So11111111111111111111111111111111111111112':
                                                    baseQuoteName = "SOL"
                                                else:
                                                    baseQuoteName = baseQuote
                                                button_trade = telebot.types.InlineKeyboardButton('Trade', url=bonkBotLink)
                                                button_birdeye = telebot.types.InlineKeyboardButton('BirdEye', url=birdEyeLink)
                                                keyboard = telebot.types.InlineKeyboardMarkup()
                                                keyboard.add(button_trade)
                                                keyboard.add(button_birdeye)
                                                constructStr = f"""
*{tokenQuoteSymbol} - Raydium Pair Found!*

Token Name : {tokenQuoteName}
Token Address : `{tokenQuote}`
Pair : {tokenQuoteSymbol} - {baseQuoteName}
Block Time : {currentTime}
Message Time : {datetime.fromtimestamp(time.time(), tz=None)}

Powered by Retina
"""
                                                if tokenQuoteIcon:
                                                    bot.send_photo(-1002110518878, tokenQuoteIcon, constructStr, parse_mode='markdown', reply_markup=keyboard)
                                                else:
                                                    bot.send_message(-1002110518878, constructStr, parse_mode='markdown', reply_markup=keyboard)
                                                print(txHash, tokenQuote, baseQuote)
                                        break
                                    except:
                                        tries.append('')
                                        print(e)
                                        print("OP Exception")
                                        if len(tries) > 50:
                                            tries.clear()
                                            break
                                        continue
            orderbookLastTx = requests.get("https://api.solscan.io/v2/account/transaction?address=srmqPvymJeFKQ4zGQed1GFppgkRHL9kaELCbyksJtPX&limit=500&cluster=", headers=headers).json()
            for i in orderbookLastTx['data']:
                if i['status'] != 'Fail':
                    for t in i["parsedInstruction"]:
                        if t['type'].lower() == 'initializemarket':
                            if True:
                                print(i['txHash'])
                                button_solscan = telebot.types.InlineKeyboardButton('Solscan', url="https://solscan.io/tx/"+i["txHash"])
                                keyboard = telebot.types.InlineKeyboardMarkup()
                                keyboard.add(button_solscan)
                                constructStr = f"""
*Found Tx Signature of InitializeMarket - Openbook*

Transaction Hash : `{i['txHash']}`
"""
                                bot.send_message(-1002110518878, constructStr, parse_mode='markdown', reply_markup=keyboard)
                                txHash = i['txHash']
                                while True:
                                    try:
                                        txnInfo = requests.get('https://api.solscan.io/v2/transaction?tx='+txHash, headers=headers).json()
                                        for k in txnInfo['data']['parsedInstruction']:
                                            if k['type'] == 'initializeMarket':
                                                currentTime = datetime.fromtimestamp(txnInfo["data"]["blockTime"], tz=None)
                                                baseQuote = k['params']['quoteMint']
                                                tokenQuote = k['params']['baseMint']
                                                tokenQuoteC = tokenQuote
                                                if baseQuote != 'So11111111111111111111111111111111111111112':
                                                    tokenQuote = baseQuote
                                                    baseQuote = tokenQuoteC
                                                tokenQuoteInfo = requests.get('https://api.solscan.io/v2/token/meta?token='+tokenQuote, headers=headers).json()
                                                tokenQuoteSymbol = tokenQuoteInfo['data']['symbol']
                                                try:
                                                    tokenQuoteIcon = tokenQuoteInfo['data']['icon']
                                                except:
                                                    tokenQuoteIcon = None
                                                tokenQuoteName = tokenQuoteInfo['data']['name']
                                                birdEyeLink = "https://birdeye.so/token/"+tokenQuote
                                                bonkBotLink = 'https://t.me/neo_bonkbot?start=ref_m8gai_ca_'+tokenQuote
                                                if baseQuote == 'So11111111111111111111111111111111111111112':
                                                    baseQuoteName = "SOL"
                                                else:
                                                    baseQuoteName = baseQuote
                                                button_trade = telebot.types.InlineKeyboardButton('Trade', url=bonkBotLink)
                                                button_birdeye = telebot.types.InlineKeyboardButton('BirdEye', url=birdEyeLink)
                                                keyboard = telebot.types.InlineKeyboardMarkup()
                                                keyboard.add(button_trade)
                                                keyboard.add(button_birdeye)
                                                constructStr = f"""
*{tokenQuoteSymbol} - Openbook Pair Found!*

Token Name : {tokenQuoteName}
Token Address : `{tokenQuote}`
Pair : {tokenQuoteSymbol} - {baseQuoteName}
Block Time : {currentTime}
Message Time : {datetime.fromtimestamp(time.time(), tz=None)}

Powered by Retina
"""
                                                if tokenQuoteIcon:
                                                    bot.send_photo(-1002110518878, tokenQuoteIcon, constructStr, parse_mode='markdown', reply_markup=keyboard)
                                                else:
                                                    bot.send_message(-1002110518878, constructStr, parse_mode='markdown', reply_markup=keyboard)
                                                print(txHash, tokenQuote, baseQuote)
                                        break
                                    except Exception as e:
                                        tries.append('')
                                        print(e)
                                        print("OP Exception")
                                        if len(tries) > 5:
                                            tries.clear()
                                            break
                                        continue
    except:
        continue
