import OlivOS
import imageSearch

def deleteBlank(str):
    str_list = list(filter(None,str.split(" ")))
    return str_list

def unity_reply(plugin_event, Proc):
    command_list = deleteBlank(plugin_event.data.message)

    if len(command_list) == 2:
        if command_list[0].lower() == "/imgs":
            response = imageSearch.image.searchImagebyUrl(command_list[1])
            plugin_event.reply(response)

