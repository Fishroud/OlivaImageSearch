'''
  _                             _____                     _     
 (_)                           / ____|                   | |    
  _ _ __ ___   __ _  __ _  ___| (___   ___  __ _ _ __ ___| |__  
 | | '_ ` _ \ / _` |/ _` |/ _ \\___ \ / _ \/ _` | '__/ __| '_ \ 
 | | | | | | | (_| | (_| |  __/____) |  __/ (_| | | | (__| | | |
 |_|_| |_| |_|\__,_|\__, |\___|_____/ \___|\__,_|_|  \___|_| |_|
                     __/ |                                      
                    |___/                                       
@File      :   imageSearch/main.py
@Author    :   Fishroud鱼仙
@Contact   :   fishroud@qq.com
@Desc      :   None

'''
import OlivOS
import imageSearch

class Event(object):
    def init(plugin_event, Proc):        
        pass

    def private_message(plugin_event, Proc):
        pass

    def group_message(plugin_event, Proc):
        imageSearch.msgReply.unity_reply(plugin_event, Proc)

    def poke(plugin_event, Proc):
        pass

    def save(plugin_event, Proc):
        pass