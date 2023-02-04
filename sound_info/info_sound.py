from gtts import gTTS
from playsound import playsound
import os
import time
import datetime

now = datetime.datetime.now()

print()
print( "Текущая дата и время с использованием метода str:")
print (str(now))
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print (now.isoformat())



while True:
    now = datetime.datetime.now()
    #time.sleep(10)
    '''
    if now.strftime("%S") == "00":
        print(now.strftime("%d-%m-%Y %H:%M:%S"))
        data = now.strftime("%H:%M:%S")
        s = gTTS("Сейчас " + data , lang='ru')
        s.save('sample1.mp3')
        playsound('sample1.mp3')
        time.sleep(5)
        os.remove('sample1.mp3')
    '''
    
    if now.strftime("%M") == "55":
        s = gTTS("Пора сделать разминку" , lang='ru')
        s.save('sample.mp3')
        playsound('sample.mp3')
        time.sleep(3)
        os.remove('sample.mp3')

    if now.strftime("%M") == "00" and (now.strftime("%H") >= '08' or now.strftime("%H") <= '18'):
        s = gTTS("Продолжаем работу" , lang='ru')
        s.save('sample.mp3')
        playsound('sample.mp3')
        time.sleep(30)
        os.remove('sample.mp3')

    if now.strftime("%H:%M") == "13:00":
        s = gTTS("Пора обедать" , lang='ru')
        s.save('sample.mp3')
        playsound('sample.mp3')
        time.sleep(30)
        os.remove('sample.mp3')
        
