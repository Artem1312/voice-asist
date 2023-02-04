from gtts import gTTS
from playsound import playsound
import os
import time
import datetime
import schedule
import time


def make_rest():
    now = datetime.datetime.now()
    # print(now.strftime("%H:%M"))
    phrase = now.strftime("%H:%M") + ' ' + 'Пора сделать разминку'
    s = gTTS(phrase , lang='ru')
    s.save('sample.mp3')
    playsound('sample.mp3')
    time.sleep(3)
    os.remove('sample.mp3')


def have_dinner():
    now = datetime.datetime.now()
    phrase = now.strftime("%H:%M") + ' ' + 'Пора обедать'
    s = gTTS(phrase , lang='ru')
    
    s.save('sample.mp3')
    playsound('sample.mp3')
    time.sleep(3)
    os.remove('sample.mp3')


def continue_work():
    s = gTTS("Продолжаем работу" , lang='ru')
    s.save('sample.mp3')
    playsound('sample.mp3')
    time.sleep(30)
    os.remove('sample.mp3')


schedule.every().hour.at(":55").until("19:30").do(make_rest)
schedule.every().hour.at(":00").until("18:30").do(continue_work)
schedule.every().day.at("13:30").do(have_dinner)

while True:
    schedule.run_pending()
    time.sleep(1)
