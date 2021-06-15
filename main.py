import time
from multiprocessing import Process
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import datetime

vk_session = VkApi(token='1c563f747be6f1d7be97f700d7779427031efdc03d16c4a62419351008dff24b309ca39ff5253215955d8')
longpoll = VkBotLongPoll(vk_session, '193242871')
vk = vk_session.get_api()


def answer(sleep_time):
    time.sleep(sleep_time)
    # print('1')
    COMMANDS = ['Кызлар', 'Козлов вернись']
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            if (event.object['text'] == COMMANDS[0]) or (event.object['text'] == COMMANDS[1]):
                vk.messages.send(
                    random_id=get_random_id(),
                    peer_id=event.obj['peer_id'],
                    message=f'{time_ask()} братка'
                )
                print(event.obj['peer_id'])


def day(sleep_time):
    while True:
        per_day()
        time.sleep(sleep_time)
        # print("12")


def per_day():
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=['2000000003'],
        message=f'Вернусь через {time_ask()}'
    )


def time_ask():
    while True:
        # year = datetime.now()  # год текущий
        try:
            start_date = datetime.date.today()
            end_date = datetime.date(2022, 6, 1)
            fin_time = str((end_date - start_date).days)
            if int(fin_time[-1]) == 1:
                return f'{(end_date - start_date).days} день'
            elif (int(fin_time[-1]) == 2) or (int(fin_time[-1]) == 3):
                if int(fin_time[-1]) == 4:
                    return f'{(end_date - start_date).days} дня'
            elif (int(fin_time[-1]) == 5) or (int(fin_time[-1]) == 6):
                if (int(fin_time[-1]) == 7) or (int(fin_time[-1]) == 8):
                    if (int(fin_time[-1]) == 9) or (int(fin_time[-1]) == 0):
                        return f'{(end_date - start_date).days} дней'
        except ValueError as err:
            print(err)
        else:
            break


if __name__ == '__main__':
    th1 = Process(target=answer, kwargs={'sleep_time': 1})
    th2 = Process(target=day, kwargs={'sleep_time': 86400})
    th1.start()
    th2.start()

    th1.join()
    th2.join()
