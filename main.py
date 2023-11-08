import re
import asyncio
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import tok, hello
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from keyboards import main, nick, success





vk = vk_api.VkApi(token = tok)
give = vk.get_api()
longpoll = VkLongPoll(vk)

print(hello)

bandits = 0

def sendmsg(id, text):
    vk.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})

def sendkey(id, text, key):
    vk.method('messages.send', {'user_id' : id, 'message' : text, 'keyboard' : key.get_keyboard(), 'random_id': 0})

def convertver_yt(text):
    def replace_link(match):
        video_id = match.group(2)
        return f'[MEDIA=youtube]{video_id}[/MEDIA]'

    # Замена ссылок в тексте
    result = re.sub(r'(https:\/\/(?:youtu\.be\/|www\.youtube\.com\/watch\?v=)([A-Za-z0-9_-]+))(?:&[^ ]*)?', replace_link, text)

    return result

# Слушаем longpoll (Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            message = event.text.lower()
            id = event.user_id
            print(message)

            if message == 'начать':
                sendkey(id, 'Привет, бот создан для помощи в Форум Варах на 20 сервере.', main)

            elif message == 'создать жалобу на бандита/лидера☢':
                sendmsg(id, 'Просто следуй следующим инструкциям!\nЯ буду просить скинуть все по форме(именно данные, все остальное я сделаю сам).')
                sendmsg(id, 'Отправь свой ник: ')
                bandits = 1



            elif bandits == 1:
                Name = event.text
                sendkey(id, f'Ваш ник: {Name}?', nick)
                bandits = 0
            elif bandits == 0 and message == 'да✅':
                sendmsg(id, 'Введите ник нарушителя: ')
                bandits = 2
            elif bandits == 0 and message == 'нет⛔':
                sendkey(id, 'Вы возращенны в главное меню!', main)
            
            elif bandits == 2:
                VragName = event.text
                sendkey(id, f'Ник нарушителя: {VragName}?', nick)
                bandits = 3
            elif bandits == 3 and message == 'да✅':
                sendmsg(id, 'Введите причину и док-ва в формате: "hif, https://www.youtube.com/...."')
                bandits = 4
            elif bandits == 3 and message == 'нет⛔':
                sendkey(id, 'Вы возращенны в главное меню!', main)
                
            elif bandits == 4:
                sendkey(id, 'Как отправите всё, нажмите снизу кнопку!', success)
                DocVa = event.text
                matches = re.findall(r'([^"]+), (https://[^\s]+)', DocVa)
                for match in matches:
                    reason = match[0]
                    evidence = match[1]
                bandits = 5
                
            elif message == 'готово✅' and bandits == 5:
                #from forms import bandit
                doc = convertver_yt(evidence)
                bandit = f'''
                Форма для заголовка темы:
                Жалоба на игрока Nick_Name [на англ] : "{VragName}" | Причина: "{reason}".

                Форма для заявки:
                Ваш игровой Nick_Name [на англ]: "{Name}".
                Игровой Nick_Name [на англ] нарушителя: "{VragName}".
                Суть жалобы: "{reason}".
                Доказательства: "{doc} ".
                Тайм-код нарушения на видео [Если фрапс идет больше 1 минуты]:
                Тайм-код /id и TAB [Если фрапс идет больше 1 минуты]:'''
                sendmsg(id, bandit)
                

