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