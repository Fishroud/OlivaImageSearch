'''
  _                             _____                     _     
 (_)                           / ____|                   | |    
  _ _ __ ___   __ _  __ _  ___| (___   ___  __ _ _ __ ___| |__  
 | | '_ ` _ \ / _` |/ _` |/ _ \\___ \ / _ \/ _` | '__/ __| '_ \ 
 | | | | | | | (_| | (_| |  __/____) |  __/ (_| | | | (__| | | |
 |_|_| |_| |_|\__,_|\__, |\___|_____/ \___|\__,_|_|  \___|_| |_|
                     __/ |                                      
                    |___/                                       
@File      :   imageSearch/msgReply.py
@Author    :   Fishroud鱼仙
@Contact   :   fishroud@qq.com
@Desc      :   None

'''
import OlivOS
import imageSearch

import time
import re

def deleteBlank(str):
    str_list = list(filter(None,str.split(" ")))
    return str_list

def unity_reply(plugin_event, Proc):
    command_list = deleteBlank(plugin_event.data.message)
    matchUrl = re.search( r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', command_list[0])

    if len(command_list) == 1:
        names = globals()
        key = 'input' + str(plugin_event.data.sender['user_id'])
        if key in names.keys() and names[key]['sender'] == plugin_event.data.sender['user_id']:
            now_time = int(time.time())
            time_diff = now_time - names[key]['time']
            if time_diff < 30:
                if matchUrl:
                    plugin_event.reply(imageSearch.image.searchImagebyUrl(matchUrl.group(0)))
                    del names[key]
            else:
                del names[key]


        elif command_list[0].lower() == "/imgs":
            plugin_event.reply("请发送待查询的图片(ゝ∀･)☆")
            names = globals()
            names['input' + str(plugin_event.data.sender['user_id'])] = {'time':int(time.time()),'sender':plugin_event.data.sender['user_id']}


    elif len(command_list) == 2:
        if command_list[0].lower() == "/imgs":
            if command_list[1].lower() == "-v"  or command_list[0].lower() == "--version":
                response = "imageSearchPlugin by Fishroud\nVersion 1.0(ﾉ)`ω´(ヾ)"
                plugin_event.reply(response)
            else:
                response = imageSearch.image.searchImagebyUrl(command_list[1])
                plugin_event.reply(response)