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

black = ["๐๐", "๐ฉแดsษช ๐ผโebserie๐ธโ๐ชโ๐ฝโโข ๐", "๐๐ฎ๐ฐ๐ธ๐๐ฝ ๐ฐ๐ต๐ฎ๐ป๐ป๐ฒ๐น :-" , "JOIN NOW ๐","Is Channel Ko Jarur Join Kare ๐", 
"Backup Channel ๐", "๐ฒ ๐บ ๐ธ ๐น  ๐ผ ๐ฆ ๐น ๐จ ๐ญโโ", "โโโโโโโโโโโโโโโโโโโโ", "--------------------------------------------------------------","โ๏ธโโโโโโโโโโโโโโโโโโ๏ธ", "Search @ Backup_villa", "๐Join For Adult Videos 18+๐","@vmlinks", "๐ข Join Our Backup Channel ๐๐", " โฌโฌโฌโฌโฌโฌโฌโฌโโโโโฌโฌโฌโฌโฌโฌโฌโฌโฌ", "๐๐๐จ๐ฐ ๐๐จ ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐"," None","https://www.instagram.com/haq.sebakchodi/", "๐๐ผ๐น๐น๐ผ๐ ๐ผ๐๐ฟ ๐ถ๐ป๐๐๐ฎ ๐ฝ๐ฎ๐ด๐ฒ๐", " ๐โโ Join Our Backup:- @AllPrivateLinkx", "All More Desi Videos:-","JOIN SPECIAL COLLECTION ๐๐","Special collection ๐๐๐๐ฆ๐ฆ๐ฆ", "DESI MASTI ๐๐ฆ๐ฆ๐ฆ"," ๐ ๐๐ก๐๐ซ๐ ๐๐ง๐ ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ ๐", "Our all channels๐@Getnewxxx_Backup", "Desi๐ -", "Foreign ๐-", "๐ฅ๐๐จ๐ข๐ง ๐๐ก๐๐ง๐ง๐๐ฅ๐ฅ", " โโโโโโโโโโโโโโโโโ", "join backup channel must", "Indian Channels๐", " English Channel ๐", "All Channels Link๐", " IMO - CHANNEL ๐๐", "----------------------------------------", "New Indian 18+ ๐๐", " ๐งโ๐ฆโ๐จโ๐ฐโ๐บโ๐ตโโ ๏ธ:-", "SHARE OUR CHANNEL๐", "โ๏ธโโโโโโโโโโโโโโโโโโ๏ธ", " Search @ Backup_villa ", " ๐ด Join Our All Other Channels ๐ด", "๐Join For Adult Videos 18+๐", "โโพโโโผโพโโโผโพโโโผโพ โโโผโพโโโผโพโโโผโ", " ๐ฅ  ๐๐๐๐ ๐๐ :โ @ViralHouse", "โ----------------------------------------------------โ", " ๐", "๐๐ฉ๐ถ๐ฟ@๐น ๐ฏ ๐ฉ๐ถ๐ฑโฌ๐ผ๐๐๐๐"]


##### ios new  ########
#desi vars
deschat = [-1001152531253,-1001376870525,-1001782270836,-1001124594300,-1001198221154,-1001184354892,-1001365203199,-1001314689320,-1001384606870,-1001691956983,-1001697964934,-1001372777220,-1001303095255,-1001461291601,-1001211071657]
iosNewD = -1001146630538

#webseries var 
webchat = [-1001663893158,-1001211406660,-1001112334078,-1001222679971]
webchat_to = -1001591437219

#eng variables
indchats = [-1001734963159,-1001143161921,-1001293319370,-1001426524321,-1001152531253,-1001182282219]
indsend_to1 = -1001692394120

#onlyfans vars  
onchat = [-1001338980365,-1001250363281,-1001569156781,-1001633880399,-1001328773456,-1001577675291,-1001597837086]
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
        caption = re.sub("๐๐ผ๐น๐น๐ผ๐ ๐ผ๐๐ฟ ๐ถ๐ป๐๐๐ฎ ๐ฝ๐ฎ๐ด๐ฒ๐" , "" , caption)
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
        caption = re.sub("๐๐ผ๐น๐น๐ผ๐ ๐ผ๐๐ฟ ๐ถ๐ป๐๐๐ฎ ๐ฝ๐ฎ๐ด๐ฒ๐" , "" , caption)
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
#         caption = re.sub("๐๐ผ๐น๐น๐ผ๐ ๐ผ๐๐ฟ ๐ถ๐ป๐๐๐ฎ ๐ฝ๐ฎ๐ด๐ฒ๐" , "" , caption)
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




