import json
import random
import time
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import sys
from vk_api.longpoll import VkLongPoll, VkEventType
token = "*"
vk = vk_api.VkApi(token=token)
vk._auth_token()
samp_sp = ['samp', 'самп']
csgo = ['ксго', 'csgo', 'cs:go', 'кс:го']
s = "Выбери и напиши нужный пункт: "
csgo_k = "ахк (не читы), читы."
samp_k = "клео, чистая гта + самп"
cleo = ['сбив анимации - https://yadi.sk/d/GYj1iaWHCnMYfA', 'аим - https://yadi.sk/d/GE2Ox1UdXiCHCA',
        'антиотдача - https://yadi.sk/d/9dv4xgRbPsXgnw', 'антидб - https://yadi.sk/d/7rpl4rrTGXkmaw',
        'бесконечный бег - https://yadi.sk/d/3UTwr4wv573-uA', 'быстрая смерть - https://yadi.sk/d/5U4WUOJqerEddw',
        'антипадение - https://yadi.sk/d/BT6Tw9Fhe8kXTw', 'anticrash - https://yadi.sk/d/-y6ZGJ3lydf1wA']
m = 'Если хочешь вернуться к выбору игр, напиши "menu"'
choise = "Выбери и напиши игру из списка доступных:"
games = ['CS:GO', 'SAMP']
antistill = "Перед скачиванием клео рекомендуем скачать антистиллер" \
            " и проверять файлы там - https://yadi.sk/d/hbfL-lxcXKWImg"


def start():
    while True:
        try:
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
            if messages["count"] >= 1:
                id = messages["items"][0]["last_message"]["from_id"]
                body = messages["items"][0]["last_message"]["text"]
                if body.lower() in samp_sp:
                    vk.method("messages.send",
                              {"peer_id": id, "message": s + samp_k,  "random_id": random.randint(1, 2147483647)})
                    vk.method("messages.send",
                              {"peer_id": id, "message": m, "random_id": random.randint(1, 2147483647)})
                    samp()
                elif body.lower() in csgo:
                    vk.method("messages.send",
                              {"peer_id": id, "message": "Раздел в разработке",
                               "random_id": random.randint(1, 2147483647)})
                    vk.method("messages.send",
                              {"peer_id": id, "message": m, "random_id": random.randint(1, 2147483647)})
                else:
                    vk.method("messages.send",
                              {"peer_id": id, "message": "Не понял тебя!",  "random_id": random.randint(1, 2147483647)})
        except Exception as E:
            time.sleep(1)


def samp():
    while True:
        try:
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
            if messages["count"] >= 1:
                id = messages["items"][0]["last_message"]["from_id"]
                body = messages["items"][0]["last_message"]["text"]
                if body.lower() == "клео":
                    for i in cleo:
                        vk.method("messages.send",
                                {"peer_id": id, "message": i,  "random_id": random.randint(1, 2147483647)})
                    vk.method("messages.send",
                              {"peer_id": id, "message": m, "random_id": random.randint(1, 2147483647)})
                    vk.method("messages.send",
                              {"peer_id": id, "message": m, "random_id": random.randint(1, 2147483647)})
                elif body.lower() == "menu":
                    vk.method("messages.send",
                              {"peer_id": id, "message": choise, "random_id": random.randint(1, 2147483647)})
                elif body.lower() == "чистая гта + samp":
                    vk.method("messages.send",
                              {"peer_id": id, "message": 'Раздел в разработке',
                               "random_id": random.randint(1, 2147483647)})
                    for i in games:
                        vk.method("messages.send",
                                  {"peer_id": id, "message": i, "random_id": random.randint(1, 2147483647)})
                    start()
                else:
                    vk.method("messages.send",
                              {"peer_id": id, "message": "Не понял тебя!",  "random_id": random.randint(1, 2147483647)})
        except Exception as E:
            time.sleep(1)


start()