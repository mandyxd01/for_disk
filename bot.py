import re
from time import sleep
import requests
from telethon import TelegramClient , events
import os
from telethon.sessions import StringSession


id= 14295855
hash = "d7c97d558577a8633485c557a41174ef"

print("Starting Deployment..!")
client = TelegramClient("main2str" , api_id=id , api_hash=hash)

#mdiskapi
mdisk_api = 'jNgyWyCG2KK4tvh5RVFX'
# sapi= '1832790492-eakHGycryH'
#footer
footer = ''' '''

black = ["👇👇", "🇩ᴇsɪ 🇼‌ebserie🇸‌🇪‌🇽‌™ 🔞", "𝗕𝗮𝗰𝗸𝘂𝗽 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 :-" , "JOIN NOW 😍","Is Channel Ko Jarur Join Kare 🙈", 
"Backup Channel 🙈", "🇲 🇺 🇸 🇹  🇼 🇦 🇹 🇨 🇭‌‌", "━━━━━━━━━━━━━━━━━━━━", "--------------------------------------------------------------","⚔️━━━━━━━━━━━━━━━━━⚔️", "Search @ Backup_villa", "🔞Join For Adult Videos 18+🔞","@vmlinks", "💢 Join Our Backup Channel 👇👇", " ▬▬▬▬▬▬▬▬☆☆☆☆▬▬▬▬▬▬▬▬▬", "👍𝐇𝐨𝐰 𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝"," None","https://www.instagram.com/haq.sebakchodi/", "𝗙𝗼𝗹𝗹𝗼𝘄 𝗼𝘂𝗿 𝗶𝗻𝘀𝘁𝗮 𝗽𝗮𝗴𝗲👇", " 🙆‍♀ Join Our Backup:- @AllPrivateLinkx", "All More Desi Videos:-","JOIN SPECIAL COLLECTION 👇👇","Special collection 🔞🔞🔞💦💦💦", "DESI MASTI 🔞💦💦💦"," 📌 𝐒𝐡𝐚𝐫𝐞 𝐀𝐧𝐝 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 📌", "Our all channels👉@Getnewxxx_Backup", "Desi💏 -", "Foreign 💏-", "🔥𝐉𝐨𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🔥", " ━━━━━━━━━━━━━━━━━", "join backup channel must", "Indian Channels🔞", " English Channel 🔞", "All Channels Link🔞", " IMO - CHANNEL 👇👇", "----------------------------------------", "New Indian 18+ 👇👇", " 🇧‌🇦‌🇨‌🇰‌🇺‌🇵‌⚠️:-", "SHARE OUR CHANNEL👇", "⚔️━━━━━━━━━━━━━━━━━⚔️", " Search @ Backup_villa ", " 🔴 Join Our All Other Channels 🔴", "🔞Join For Adult Videos 18+🔞", "●╾⁃⁃╼╾⁃⁃╼╾⁃⁃╼╾ ⁃⁃╼╾⁃⁃╼╾⁃⁃╼●", " 📥  𝐉𝐎𝐈𝐍 𝐔𝐒 :– @ViralHouse", "●----------------------------------------------------●", " 👉", "😍𝗩𝗶𝗿@𝗹 💯 𝗩𝗶𝗱€𝗼𝘀😈👇👇"]


##### ios new  ########



deschat = [-1001502261795,-1001152531253,-1001250363281,-1001376870525,-1001782270836,-1001124594300,-1001198221154,-1001184354892,-1001365203199,-1001314689320,-1001384606870,-1001691956983,-1001697964934,-1001372777220,-1001303095255,-1001461291601,-1001211071657]
iosNewD = -1001146630538

#webseries var 
webchat = [-1001314689320,-1001338980365,-1001663893158,-1001211406660,-1001222679971]
webchat_to = -1001591437219

#eng variables
indchats = [-1001644938227,-1001690938554,-1001674541893,-1001723730562,-1001662191039,-1001803156345,-1001734963159,-1001143161921,-1001293319370,-1001426524321,-1001152531253,-1001182282219]
indsend_to1 = -1001692394120

#onlyfans vars  
onchat = [-1001372777220,-1001461291601,-1001338980365,-1001569156781,-1001633880399,-1001328773456,-1001577675291,-1001597837086]
onsend_to = -1001619663914



############### ENGLISH  ##########

@client.on(events.NewMessage(chats=indchats))
async def hello1(event):

    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 
        
        caption = re.sub("hehe" , "" , caption)
        
        caption = re.sub("hoho" , "" , caption)
        caption = re.sub("𝗙𝗼𝗹𝗹𝗼𝘄 𝗼𝘂𝗿 𝗶𝗻𝘀𝘁𝗮 𝗽𝗮𝗴𝗲👇" , "" , caption)
        caption = re.sub("https://www.instagram.com/haq.sebakchodi/" , "" , caption)
        caption = re.sub("https://t.me/open_streaam/14" , "https://t.me/Watch_Streaam_Links/9" , caption)


        caption = re.sub("@.*" , "@X3Links" , caption)
        caption = re.sub("https://t.me/.*" , " " , caption)
        caption = re.sub("t.me/.*" , " " , caption)
        caption = re.sub("T.me/.*" , " " , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link.strip()
                }
            try:
                res = requests.post(url, json = param)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['sharelink']
            except:
                print("error in share")
                shareLink = ""
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            if(shareLink == "https://mdisk.me/convertor/16x9/kkIv73"):
                return
            sleep(0.2)
        caption = caption + "\n"
        if media:
            await client.send_file(indsend_to1,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(indsend_to1, caption)
            
            
            
            ###############  IOS ##########

@client.on(events.NewMessage(chats=deschat))
async def hello2(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 
        
        caption = re.sub("hehe" , "" , caption)
        
        caption = re.sub("hoho" , "" , caption)
        caption = re.sub("𝗙𝗼𝗹𝗹𝗼𝘄 𝗼𝘂𝗿 𝗶𝗻𝘀𝘁𝗮 𝗽𝗮𝗴𝗲👇" , "" , caption)
        caption = re.sub("https://www.instagram.com/haq.sebakchodi/" , "" , caption)
        caption = re.sub("https://t.me/open_streaam/14" , "" , caption)




        caption = re.sub("@.*" , "@X3Links" , caption)
        caption = re.sub("https://t.me/.*" , " " , caption)
        caption = re.sub("t.me/.*" , " " , caption)
        caption = re.sub("T.me/.*" , " " , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link.strip()
                }
            try:
                res = requests.post(url, json = param)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['sharelink']
            except:
                print("error in share")
                shareLink = ""
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            if(shareLink == "https://mdisk.me/convertor/16x9/kkIv73"):
                return
            sleep(0.2)
        caption = caption + "\n"
        if media:
            await client.send_file(iosNewD,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(iosNewD, caption)



  ##################### WEBSERIES #############  

# @client.on(events.NewMessage(chats=webchat))
# async def hello3(event):
#     # chat = await event.get_chat()
#     caption = event.message.message
#     # link syntax = https://streaam.net/S/$UydxddrFxb 
#     urls_to_change = re.findall('https?://streaam.net/S/.*' , caption)
#     # print(urls_to_change)
#     if(urls_to_change):
#         try:
#             media = await client.download_media(event.message)
#         except:
#             media = False
#             print("no media")
#         #  this is for blacklist word 

#         caption = re.sub("hehe" , "" , caption)
#         caption = re.sub("hoho" , "" , caption)
#         caption = re.sub("𝗙𝗼𝗹𝗹𝗼𝘄 𝗼𝘂𝗿 𝗶𝗻𝘀𝘁𝗮 𝗽𝗮𝗴𝗲👇" , "" , caption)
#         caption = re.sub("https://www.instagram.com/haq.sebakchodi/" , "" , caption)
   

#         caption = re.sub("@.*" , "@X3Links" , caption)
#         caption = re.sub("https://t.me/.*" , " " , caption)
#         caption = re.sub("t.me/.*" , " " , caption)
#         caption = re.sub("T.me/.*" , " " , caption)
#         for i in black:
#             caption = re.sub(i, "" , caption)
            
#         regrex_pattern = re.compile(pattern = "["
#                     u"\U0001F600-\U0001F64F"  # emoticons
#                     u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#                     u"\U0001F680-\U0001F6FF"  # transport & map symbols
#                     u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                             "]+", flags = re.UNICODE)

#         # url to change 
#         for i in urls_to_change:
#             link = regrex_pattern.sub(r'' , i)
#             linkid = link.split("/")[-1]
#             # print(linkid)
#             key = sapi
#             url  = f'https://api.streaam.net/save?linkid={linkid}&key={key}'
#             # print(url)
#             # param = {
#             #     'token': mdisk_api,
#             #     'link':link.strip()
#             #     }
#             try:
#                 res = requests.get(url)
#             except:
#                 print("error in res")
#                 return
#             try:
#                 shareLink = res.json()['link']
#             except:
#                 print("error in share")
#                 shareLink = ""
#             print("changed link : " , shareLink)
#             caption = re.sub(re.escape(i) , shareLink , caption)
#             # print(caption)
#             # sleep(0.2)
#         caption = caption
#         if media:
#             await client.send_file(websend_to ,file=media , caption=caption)
#             os.remove(media)
#         else:
#             await client.send_message(websend_to , caption)
            
            
  
############ TANGO ###############
'''
@client.on(events.NewMessage(chats=tanchat))
async def hello5(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)
        

        caption = re.sub("@.*" , "@X3Links" , caption)
        caption = re.sub("https://t.me/.*" , " " , caption)
        caption = re.sub("t.me/.*" , " " , caption)
        caption = re.sub("T.me/.*" , " " , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link.strip()
                }
            try:
                res = requests.post(url, json = param)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['sharelink']
            except:
                print("error in share")
                shareLink = ""
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(tansend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(tansend_to , caption)'''
            
            
            
            
            
            
############## WEBSERIES ######################


@client.on(events.NewMessage(chats=webchat))
async def hello5(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)
        

        caption = re.sub("@.*" , "@X3Links" , caption)
        caption = re.sub("https://t.me/.*" , " " , caption)
        caption = re.sub("t.me/.*" , " " , caption)
        caption = re.sub("T.me/.*" , " " , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link.strip()
                }
            try:
                res = requests.post(url, json = param)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['sharelink']
            except:
                print("error in share")
                shareLink = ""
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            if(shareLink == "https://mdisk.me/convertor/16x9/kkIv73"):
                return
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(webchat_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(webchat_to , caption)
           
        
        
        
 
        
########### ONLYFANS #####################
@client.on(events.NewMessage(chats=onchat))
async def hello6(event):
    # chat = await event.get_chat()
    caption = event.message.message
    urls_to_change = re.findall('https?://mdisk.me/convertor/.*' , caption)
    if(urls_to_change):
        try:
            media = await client.download_media(event.message)
        except:
            media = False
            print("no media")
        #  this is for blacklist word 
        caption = re.sub("hehe" , "" , caption)
        caption = re.sub("hoho" , "" , caption)
        

        caption = re.sub("@.*" , "@X3Links" , caption)
        caption = re.sub("https://t.me/.*" , " " , caption)
        caption = re.sub("t.me/.*" , " " , caption)
        caption = re.sub("T.me/.*" , " " , caption)
        for i in black:
            caption = re.sub(i, "" , caption)

        regrex_pattern = re.compile(pattern = "["
                    u"\U0001F600-\U0001F64F"  # emoticons
                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags = re.UNICODE)

        # url to change 
        for i in urls_to_change:
            link = regrex_pattern.sub(r'' , i)
            #print(link)
            url  = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
            param = {
                'token': mdisk_api,
                'link':link.strip()
                }
            try:
                res = requests.post(url, json = param)
            except:
                print("error in res")
                return
            try:
                shareLink = res.json()['sharelink']
            except:
                print("error in share")
                shareLink = ""
            # print("changed link : " , shareLink)
            caption = re.sub(link , shareLink , caption)
            # print(caption)
            if(shareLink == "https://mdisk.me/convertor/16x9/kkIv73"):
                return
            sleep(0.2)
        caption = caption + "\n" + footer
        if media:
            await client.send_file(onsend_to ,file=media , caption=caption)
            os.remove(media)
        else:
            await client.send_message(onsend_to , caption)



    
print("Bot has been deployed.!")

client.start()
client.run_until_disconnected()




